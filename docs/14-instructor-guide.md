# 14 教学使用说明

## 课程定位

本仓库适合两类课程：

- 16 到 32 学时的 LLM serving 系统导论；
- 8 到 12 周的软件工程 capstone。

前者聚焦 core、messages、KV cache、scheduler 和 serving；后者增加模型、kernel、TP 和性能研究。

## 不建议直接展示答案

git 历史保留了原始实现。建议课程流程：

1. 学生先阅读脚手架和本章问题；
2. 运行练习得到 failure；
3. 独立写最小实现与边界测试；
4. 完成自评后，再对照上游设计；
5. 在评审中解释差异，而不是只比较行数。

## 分阶段解锁

可以按以下顺序开放目录：

| 周次 | 开放范围 | 交付 |
|---|---|---|
| 1 | docs + utils + core | 数据模型和测试 |
| 2 | message + table | 消息协议与状态机 |
| 3-4 | kvcache | Naive/Radix + 属性测试 |
| 5 | scheduler | prefill/decode/chunk |
| 6-7 | models + layers | 单层与单模型 |
| 8 | engine | greedy 生成 |
| 9 | server | OpenAI API |
| 10 | performance | 报告与评审 |

## 评分重点

- 能否说明不变量，而不是只会通过测试；
- 错误路径和资源释放是否覆盖；
- 是否先建立 reference；
- 是否区分环境跳过与实现失败；
- 性能结论是否可复现；
- 是否能承认未完成的高级模块。

## 课堂讨论题

1. 为什么 cache handle 不能只返回命中长度？
2. chunked prefill 为什么比简单限制 batch size 更难？
3. paged KV 与 OS 虚拟内存的异同是什么？
4. overlap scheduling 省掉的是 CPU 时间还是 GPU 时间？
5. TP 中哪个算子需要 all-reduce，哪个只需要本地计算？
6. CUDA Graph 为什么偏好固定 batch size？
7. detokenize 为什么必须增量处理 UTF-8？
8. 什么时候 abort 的幂等性尤其重要？

## 维护脚手架

如果新增模块：

1. 添加最小契约和 `NotImplementedError`；
2. 在 [仓库与模块地图](03-code-map.md) 标注章节；
3. 添加 smoke inventory 条目；
4. 添加一个 exercise 或说明为何暂不测试；
5. 运行默认 pytest。

课程答案建议放在单独、非默认分支或私有评测系统，避免污染学生基线。
