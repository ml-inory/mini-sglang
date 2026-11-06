# 结课项目

结课目标不是复刻上游所有优化，而是完成一条可解释、可测试、可测量的最小 LLM serving 路径。

## 必做范围

1. 请求与消息模型；
2. 一个可用的 naive 或 radix prefix cache；
3. page table 与 KV cache pool；
4. 单进程 prefill/decode 调度；
5. 一个支持 causal attention 的小模型；
6. greedy sampling；
7. OpenAI 兼容 non-stream 接口；
8. 单元、集成和资源回收测试；
9. 一份性能报告。

## 选做范围

- chunked prefill；
- Radix 节点 split 与淘汰；
- overlap scheduling；
- CUDA Graph；
- stream API；
- TP=2；
- FlashInfer/FlashAttention；
- MoE；
- CUDA/Triton kernel。

## 里程碑

### M0：环境与基线

- 默认 `pytest` 通过；
- 记录 Python、PyTorch、CUDA 和硬件；
- 能解释本机可完成哪些章节。

### M1：核心状态

- `Req`、`Batch`、`Context` 不变量测试通过；
- 消息 round-trip 通过；
- 无资源泄漏。

### M2：KV cache

- 单 page 与多 page 分配测试通过；
- 相同 prefix 第二次请求减少 prefill token；
- 活跃请求不会被淘汰；
- integrity check 通过。

### M3：调度器

- prefill 到 decode 完整切换；
- 多请求 batch；
- abort 和完成均只释放一次；
- 容量不足有确定策略。

### M4：模型执行

- 单层 CPU reference 通过；
- 小模型 greedy 可重复；
- 权重映射有缺失/多余检查。

### M5：服务

- `/v1/models` 与 `/v1/chat/completions` schema 通过；
- stream 与 non-stream 一致；
- 客户端断开可取消请求。

### M6：性能

- 固定 workload；
- 报告 TTFT、ITL、吞吐、显存；
- 至少做一次单因素消融；
- 保留原始数据与命令。

## 最终演示

准备一个不超过 15 分钟的演示：

1. 画出系统架构和请求时序；
2. 展示一个共享前缀请求如何命中 cache；
3. 展示一次 chunked prefill 或 abort；
4. 展示测试输出；
5. 展示性能基线与一次消融；
6. 说明一个失败尝试和从中得到的结论。

## 评分建议

| 维度 | 权重 | 证据 |
|---|---:|---|
| 正确性 | 30% | 单元、集成、边界测试 |
| 资源安全 | 20% | cache lock、abort、release、integrity |
| 设计解释 | 20% | 架构图、状态图、代码评审 |
| 可观测性 | 15% | 日志、指标、错误信息 |
| 性能方法 | 15% | 基线、环境、稳定性、消融 |

只获得高吞吐但没有正确性和资源证据，不计为优于慢而正确的实现。

## 提交清单

- [ ] 所有必做练习通过；
- [ ] 默认 smoke 仍通过；
- [ ] 代码不引入必需的重型 import；
- [ ] README 更新运行命令；
- [ ] docs 更新架构决策；
- [ ] 无模型文件、trace 或编译缓存被提交；
- [ ] 性能报告包含 commit hash；
- [ ] 能明确列出未实现项和风险。
