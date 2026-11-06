# 性能实验：先证明正确，再证明更快

性能优化不是“看起来更复杂”。每次变更都应包含假设、基线、对照、指标和回归门槛。

## 核心指标

- **TTFT**：请求到首 token 的延迟，主要受排队、prefill 和 detokenize 影响。
- **ITL**：相邻输出 token 的间隔，观察 decode 稳定性。
- **总延迟**：请求提交到完整回复。
- **请求吞吐**：每秒完成请求数。
- **token 吞吐**：每秒输入加输出 token 数。
- **有效吞吐**：在延迟 SLO 内完成的 token 数。
- **显存峰值**：权重、KV cache、workspace 和 graph 分开记录。
- **缓存命中复用 token 比例**：不能只报告 cache 容量。

## 离线实验

离线 benchmark 一次性提交固定 workload。适合研究 throughput、batching 和缓存复用。

必须固定：

- 模型版本与精度；
- 随机种子；
- 输入/输出长度分布；
- 请求数；
- warmup；
- 预热后的测量区间；
- CPU、GPU、驱动和容器镜像。

## 在线实验

在线 trace 重放应包含到达时间或并发模型。需要报告：

- 并发数随时间变化；
- p50/p95/p99 TTFT；
- p50/p95/p99 ITL；
- 完成率与错误率；
- 队列等待时间；
- 端到端吞吐。

只报告平均值会掩盖长尾；LLM 服务用户体验通常由 p95/p99 决定。

## 消融设计

可用环境变量或配置对比：

- overlap scheduling on/off；
- naive cache 与 radix cache；
- page size 1/4/8/16；
- chunked prefill budget；
- attention backend；
- CUDA Graph on/off；
- TP 1/2/4。

每次只改变一个因素。性能提升同时伴随正确性变化时，该结果无效。

## 测量陷阱

- 忘记 `torch.cuda.synchronize()`，得到的是 launch 时间；
- 首次 JIT 编译混入 steady-state；
- cache 热态与冷态混合；
- 客户端成为瓶颈；
- 只测短输出，忽略 decode 长尾；
- page 分配器碎片导致“同样的平均长度”表现不同；
- padding 导致小 batch 也执行大 graph；
- 多卡 benchmark 没确认所有 rank 完成。

## 实验记录模板

```markdown
## Hypothesis
Change X should improve metric Y because Z.

## Environment
GPU, driver, CUDA, PyTorch, model, commit, command.

## Workload
Requests, input/output distribution, concurrency, random seed.

## Baseline
p50, p95, p99, throughput, peak memory, correctness test.

## Candidate
Same fields as baseline.

## Result
Absolute and relative change with run-to-run variance.

## Decision
Keep, revise, or revert; include regression risk.
```

## 性能回归

正确性测试和大性能 benchmark 不应在每个小 commit 上全跑。建议：

- 每次 commit：纯单元和 shape 测试；
- 每日：固定小模型 smoke benchmark；
- 发布候选：完整 workload 与多卡对比；
- 性能阈值使用噪声区间，不用单次运行。

benchmark 脚本位于 `benchmark/offline` 与 `benchmark/online`。先实现可靠的计时和数据收集，再追求更复杂的 workload。
