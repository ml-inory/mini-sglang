# 04 请求与消息

本章从“用户的一句话”追踪到调度器可处理的请求对象。

## 本章作业 H04

实现 `core.py` 和 `message/` 的最小契约，覆盖长度不变量、phase 派生、消息编码/解码和未知类型错误。先完成 CPU-only 测试，再接入张量模型。

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest \
  tests/exercises/test_core.py tests/exercises/test_messages.py -q
```

## 核心对象

### `SamplingParams`

它描述生成策略，而不是模型输入。至少包含 temperature、top-k、top-p、最大 token 数和 EOS 忽略策略。`is_greedy` 是派生属性，不能复制成容易失去同步的独立字段。

### `Req`

`Req` 是调度器拥有的可变请求状态。建议先锁定以下语义：

- `input_ids` 是 CPU 上的 token 序列；
- `cached_len` 表示已经稳定写入 KV cache 的 token 数；
- `device_len` 表示当前请求已经推进到的序列长度；
- `max_device_len` 等于输入长度加最大输出长度；
- `extend_len = device_len - cached_len`；
- `remain_len = max_device_len - device_len`。

一次 decode 采样的常见推进方式是：先把旧的 `device_len` 标记为已缓存，再增加一个新 token。你要明确“cached”与“computed”是否是同一时刻，并在所有测试中保持一致。

### `Batch`

Batch 是调度器交给 engine 的一次计算计划：

- `phase` 只能是 prefill 或 decode；
- `reqs` 保存真实请求顺序；
- `padded_reqs` 为 CUDA Graph 或 kernel 形状约束补空请求；
- `positions`、`out_loc`、`attn_metadata` 由调度准备阶段填充。

不要把这些中间字段放在 `Req` 上。它们属于一次 batch，不属于请求生命周期。

### `Context`

Context 保存一次 forward 中共享的 page table、attention backend、MoE backend 和 KV cache。它通过上下文管理器保证活动 batch 在异常时也被清理。

## 推荐实现顺序

1. 为两个长度属性写纯数学测试；
2. 实现 `Req` 的初始化和宿主 token append；
3. 实现 `Batch` 的 phase 派生属性；
4. 实现 `Context` 的单层上下文约束；
5. 最后接入真实张量存储。

测试入口：`tests/exercises/test_core.py`。

## 消息边界

系统进程之间不共享 Python 对象地址，因此每类消息都必须是可编码的数据。主要分为三层：

- frontend：API 与 tokenizer 之间的文本回复；
- tokenizer：tokenize、abort、detokenize 指令；
- backend：scheduler/engine 的 user、abort、batch、exit 指令。

消息设计必须回答：

1. 谁创建它？
2. 谁消费它？
3. 哪条路由会转发它？
4. 它是否可能被合并成 batch message？
5. 消费失败时是否会影响后续消息顺序？

## 序列化边界

`serialize_type` 与 `deserialize_type` 不是通用 pickle 的替代品，而是只覆盖系统实际传输的数据模型。实现时应明确：

- 类型标签放在哪里；
- 嵌套 dict/list/tuple 如何递归；
- bytes 是否保持原样；
- tensor 是否只允许一维；
- dtype 如何从字符串恢复；
- 未知类型是忽略、报错还是兼容升级。

永远不要反序列化不可信 pickle。当前协议应优先使用白名单类型和明确 type tag。

## 失败与顺序

至少定义以下错误策略：

- 非法消息类型：记录错误并终止当前 worker，还是跳过？
- uid 不存在：abort 是否幂等？
- 相同 uid 重复提交：拒绝还是替换？
- 流式连接中断：是否发送 abort，何时释放请求资源？
- scheduler 退出：其他进程如何得知并终止？

把策略写进测试，而不是依赖“应该不会发生”。

## 本章验收

- 能画出 tokenizer -> scheduler -> engine -> detokenizer 的消息流；
- `Req` 长度不变量有单元测试；
- 嵌套消息能 round-trip；
- 未知类型有明确错误；
- 默认导入不依赖 PyTorch；
- `test_core.py` 与 `test_messages.py` 通过。

下一章进入 [KV Cache](05-kv-cache.md)。
