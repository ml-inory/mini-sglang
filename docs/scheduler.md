# 调度器：从请求队列到计算 Batch

调度器决定“下一步计算谁、算多少、占用哪些 KV page、何时结束”。它既是资源管理器，也是状态机。

## 两种计算阶段

### Prefill

prefill 一次处理 prompt 中尚未缓存的 token。计算量随 prompt 长度增长，通常会生成完整的 query-key-value，并产生第一个输出 token。

### Decode

decode 每个运行请求只输入一个新 token，但需要读取全部历史 KV。它更偏 memory-bandwidth bound，batch 越大通常越能摊薄权重读取。

调度策略必须在延迟和吞吐之间做选择。先实现“有 prefill 就 prefill，否则 decode”，再研究 decode-priority、公平队列或 token budget 策略。

## 管理器的职责

### `TableManager`

管理每个活动请求的 table slot。每个 slot 对应 page table 中的一行和 token pool 中的一行。分配与释放必须唯一，防止两个请求写入同一行。

### `PrefillManager`

维护等待请求，并尝试把请求装入 token budget 和 KV capacity。它需要：

- 匹配已有 prefix；
- 锁定 cache handle；
- 预留预估输出长度；
- 分配 table slot；
- 决定完整 prefill 还是 chunked prefill；
- 把未完成请求放回队首或继续队。

### `ChunkedReq`

当 prompt 大于本轮 token budget 时的中间状态。它不能触发正常采样，且下一轮必须复用原来的 table、cache handle 和 cached length。

### `DecodeManager`

保存运行请求的集合，生成稳定顺序的 decode batch，并在请求结束或中止时移除。顺序稳定对多 rank 通信尤其重要。

### `CacheManager`

把逻辑长度映射到物理 page。调度器只应该通过它分配、锁定、插入和释放，不直接改 free list。

## 推荐状态机

一个请求至少经过：

```text
waiting -> prefill/chunking -> decoding -> finished
                                  |
                                  +-> aborted
```

资源释放发生在两个时刻：

1. 请求结束后释放 table slot；
2. 已完成的 KV prefix 被转入可复用缓存，不再由活动 handle 保护。

必须定义请求在“采样完成但回复尚未发出”时属于哪个状态，否则会重复释放或提前复用 slot。

## 调度单轮

可以按以下顺序实现一轮：

1. 非阻塞接收控制消息；
2. 处理新请求、abort 和 exit；
3. 先尝试 prefill，再尝试 decode；
4. 为 batch 补齐 padded 请求；
5. 分配新 page，构造 positions 和 output locations；
6. 准备 attention metadata；
7. 调用 engine forward；
8. 处理采样结果、回复、结束和释放。

每一步都应能单独测试，不要把整个流程塞进一个不可观察的函数。

## Chunked Prefill 难点

跨轮状态至少有：

- 原始 pending request；
- 当前 chunk request；
- table slot；
- prefix cache handle；
- cached length；
- 已预留的输出容量。

测试场景：

- prompt 恰好等于 budget；
- prompt 比 budget 多一个 token；
- 连续三个 chunk；
- chunk 期间收到 abort；
- chunk 期间发生 KV 淘汰压力；
- 多请求混合完整 prefill 和 chunk。

## 资源预留

调度器不能只看当前需要多少 page，还要为 decode 继续增长预留空间。否则 prefill 成功、decode 很快 OOM。

你需要定义：

- 输入 token 需要多少 page；
- 输出 max_tokens 预估多少 page；
- page 尾部的浪费如何计入；
- 已运行请求的 in-flight token 如何预留；
- 资源不足时拒绝新请求还是抢占已有请求。

## Overlap Scheduling

普通路径可以抽象为：

```text
接收消息 -> 生成 batch metadata -> GPU forward -> 处理结果
```

overlap 路径让上一轮 GPU 计算与下一轮 CPU metadata 准备并行：

```text
处理上一轮结果
      |
准备下一轮 metadata -- 同时等待上一轮 GPU
      |
提交下一轮 GPU forward
```

这不是简单的“多开一个线程”。你需要保证：

- metadata 使用的固定输入不会被 GPU 覆盖；
- CPU pinned buffer 的生命周期覆盖异步 copy；
- 结果处理发生在正确 stream 同步之后；
- 请求释放不会被上一轮和当前轮重复执行；
- 所有 rank 的 batch 顺序一致。

## 可观测性

建议在每一轮记录：

- waiting/running/finished 请求数；
- prefill token 数、decode 请求数；
- free pages、evictable pages、protected pages；
- batch 构造耗时、forward 耗时、结果处理耗时；
- 因容量不足未调度的请求数。

没有这些指标，调度优化只能靠猜。

## 本章验收

- 空队列、单请求、多请求调度测试；
- page=1 与 page>1 的资源分配测试；
- chunked prefill 跨轮通过；
- abort 后所有资源只释放一次；
- decode batch 顺序稳定；
- 能解释 overlap 路径中每个 tensor 的所有权；
- `test_table_and_decode.py` 通过。

下一章：[模型与层](models-and-layers.md)。
