# 引擎与分布式执行

调度器决定“算什么”，Engine 决定“怎样在单个 TP rank 上真正算出来”。

## Engine 的边界

`Engine` 通常拥有：

- 模型；
- page table；
- KV cache pool；
- attention backend；
- MoE backend；
- sampler；
- CUDA Graph runner；
- 当前 CUDA stream。

它不应拥有用户连接、HTTP 请求或 tokenizer 文本状态。这些属于 server 和 scheduler。

## Forward 输入与输出

Engine 接收 Batch 和采样参数，返回：

- 下一个 token；
- 用于回写的 CPU/GPU tensor；
- 可能的 logits 或采样临时状态；
- stream 同步信号。

所有异步 copy 必须回答“谁等待、何时等待”。如果 CPU 在 GPU copy 完成前读取 next token，结果会随机重复。

## Sampling

先实现 greedy，再实现 top-k、top-p 和 temperature。测试要覆盖：

- 单请求与 batch；
- EOS；
- max token 到达；
- 非法 temperature/top-p；
- 全 masked 或概率为零；
- 固定 seed 下可重复。

采样通常只在拥有权威结果的 rank 上执行，然后把 token 广播到其他 TP rank，保证下一轮输入一致。

## CUDA Graph

CUDA Graph 适合固定形状、重复 launch 的 decode。步骤：

1. 按离散 batch size 预分配静态输入；
2. capture；
3. 用真实输入 copy 到静态 buffer；
4. replay；
5. 处理尾部 pad；
6. 输出回写到真实 batch 顺序。

不能 capture 的路径包括动态 control flow、隐式同步和变化地址读取。先保留非 graph 路径作为正确性 reference。

## Graph Runner 的 padding

pad request 不参与真实状态推进，但仍需要合法 token、table 和 cache 输入，避免 kernel 访问未初始化内存。测试：

- batch size 小于最小 graph size；
- 恰好命中 graph size；
- 大于所有预捕获 size；
- padded 请求不进入 decode set；
- padded 输出不发送给用户。

## Tensor Parallel 基础

TP rank 是模型权重与计算切分，不是简单的多进程 HTTP worker。每个 rank：

- 加载自己的权重 slice；
- 接收相同请求和调度顺序；
- 执行本地计算；
- 在层内 all-reduce/all-gather；
- 共同推进请求状态；
- 只在 rank 0 暴露控制端点。

如果某个 rank 提前 break，其他 rank 会在 collective 上永久等待。

## 分布式信息与注册

`DistributedInfo` 至少包含 rank、world size、local rank 和 CPU/GPU group。初始化流程：

1. 建立 process group；
2. 生成或交换 TP 信息；
3. 校验所有 rank 的模型配置；
4. 分配各自权重；
5. 执行一次 collective smoke test；
6. 进入 scheduler/engine 循环。

`get_tp_info()`、`set_tp_info()` 和 `try_get_tp_info()` 应避免模块 import 时就初始化进程组。

## 多进程架构

典型关系：

```text
API server
   |
tokenizer worker
   |
scheduler rank 0 <----控制消息----> scheduler rank N
   |
detokenizer worker
   |
streaming response
```

ZMQ 队列负责消息；NCCL 负责张量集合通信。两种通道失败模式不同，必须分别监控。

## 失败处理

- rank 0 收到 exit 后通知所有 rank；
- 单个 rank 异常时，父进程杀掉同组 worker；
- collective 前记录 rank、operation、shape、dtype；
- stream 和 process group 都在 finally 中清理；
- 禁止在非 rank 0 输出海量日志；
- 避免只在 rank 0 做成功判断。

## 本章验收

- 单卡 engine 完成一次 prefill 和多次 decode；
- greedy 输出可重复；
- non-graph 与 graph 输出一致；
- padded batch 不污染真实请求；
- 两 rank TP smoke test 完成；
- 所有 rank 能正常退出；
- overlap 路径有明确的 stream 与 sync 测试。

下一章：[服务链路](serving.md)。
