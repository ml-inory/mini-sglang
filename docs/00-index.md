# 00 Mini-SGLang 教学仓课程首页

这个仓库不是一份可以直接部署的推理系统，而是一张可以动手重建的工程地图。原项目中的每个模块路径都被保留，类和函数签名作为接口线索存在，函数体统一等待你实现。

学习目标不是“背完所有源码”，而是建立一条完整因果链：

> 文本变成 token，token 变成请求，请求被调度成 batch，batch 通过模型和 attention 计算，KV 被缓存和复用，token 再流回用户。

## 先读这三条规则

1. **每次只改变一个可解释的层次。** 先让数据结构和纯 Python 契约通过测试，再接入 PyTorch，再考虑 CUDA。
2. **测试先于优化。** 没有正确性基线和可复现测量时，不比较吞吐、显存或延迟。
3. **硬件能力不是学习前提。** CPU 主线必须可完成；GPU、分布式和原生 kernel 是进阶模块，可以按硬件条件逐项解锁。

## 编号规则

- `00`：课程说明、阅读顺序和作业总览，先读这一页。
- `01` 到 `13`：必读主线，原则上按数字升序完成。
- `14` 到 `17`：辅助与参考资料，不要求顺序阅读。
- 作业编号 `H00` 到 `H13` 与文档编号一一对应。

## 推荐学习路径

| 编号 | 文档 | 学习重点 | 对应作业 | 最低交付物 |
|---|---|---|---|---|
| 00 | [课程首页](00-index.md) | 学习方法、顺序和验收规则 | H00 | 学习计划 |
| 01 | [环境与硬件](01-environment.md) | CPU、PyTorch、CUDA 三层环境 | H01 | 环境检查记录 |
| 02 | [基础训练](02-foundations.md) | 不变量、张量、并发、对齐和测试 | H02 | 基础工具实现 |
| 03 | [仓库与模块地图](03-code-map.md) | 子系统边界与依赖方向 | H03 | 模块依赖图 |
| 04 | [请求与消息](04-core-and-messages.md) | `Req`、`Batch`、消息和序列化 | H04 | Core 与消息测试通过 |
| 05 | [KV Cache](05-kv-cache.md) | 分页缓存、Radix Tree、lock/evict | H05 | 缓存测试与边界报告 |
| 06 | [调度器](06-scheduler.md) | prefill、decode、chunk 和资源预算 | H06 | 调度状态机测试 |
| 07 | [模型与层](07-models-and-layers.md) | Transformer 层、权重和 TP 切分 | H07 | 单层参考与模型 smoke |
| 08 | [Attention 与 Kernel](08-kernel-and-attention.md) | backend、CUDA/Triton、正确性与性能 | H08 | reference parity 报告 |
| 09 | [引擎与分布式](09-engine-and-distributed.md) | Engine、采样、Graph、NCCL 和 TP | H09 | 单卡 engine smoke |
| 10 | [服务链路](10-serving.md) | HTTP、tokenizer、流式输出和 abort | H10 | OpenAI API 集成测试 |
| 11 | [性能实验](11-performance.md) | TTFT、ITL、吞吐、显存和消融 | H11 | 可复现 benchmark 报告 |
| 12 | [测试手册](12-testing.md) | pytest 分层、边界和覆盖率 | H12 | 新增测试与覆盖率记录 |
| 13 | [结课项目](13-capstone.md) | 端到端集成与最终演示 | H13 | 可运行最小系统 |

建议每周完成一个阶段，并固定使用这一循环：阅读契约 -> 手写状态图 -> 实现最小版本 -> 运行定向测试 -> 补充边界测试 -> 写作业记录。

## 作业总表

### H00 制定学习计划

读完本页后建立个人进度表，至少写下目标、可用硬件、预计周期和打算跳过的内容。完成本章判断题中的 8 个问题后，再进入正文。

### H01 环境基线

创建虚拟环境并完成安装，保存以下证据：

```bash
python --version
python -m pytest -x -q
python -m minisgl --help
```

如果继续 GPU 章节，再记录 `nvidia-smi` 和 PyTorch CUDA 检测结果。

### H02 基础工具

阅读 [基础训练](02-foundations.md)，实现：

- `utils/misc.py` 中的对齐和除法工具；
- `utils/registry.py` 中的注册表。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_foundations.py -q
```

### H03 画出架构

不看答案，仅根据 [仓库与模块地图](03-code-map.md) 和脚手架绘制：

- API/tokenizer/scheduler/engine/detokenizer 进程图；
- core/message/cache/scheduler/model/layer/kernel 的依赖图；
- 一次请求从文本到 token 回复的时序图。

交付一张自己画出的图，并标出每个跨模块数据结构的责任方。

### H04 请求与消息

实现 `core.py` 与 `message/` 中本章要求的契约，重点覆盖长度不变量、batch phase、嵌套消息 round-trip 和未知类型错误。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_core.py tests/exercises/test_messages.py -q
```

### H05 KV Cache

依次完成 base、naive、Radix、MHA pool 和 `scheduler/cache.py`。至少补充 page size 为 `1/2/4`、共享前缀、分叉、lock 和 evict 的边界测试。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_cache.py -q
```

### H06 调度器

实现 table、decode、prefill 和主调度循环。先完成完整 prefill，再增加 chunked prefill；abort 和完成路径必须验证资源只释放一次。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_table_and_decode.py -q
```

另外提交一张状态图，覆盖 waiting、prefill、chunking、decode、finished 和 aborted。

### H07 模型与层

实现 activation、norm、RoPE、linear、embedding、attention layer 和一个最小模型。先对齐 PyTorch 参考，再处理 TP。提交单层固定输入/输出 golden case。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_layers.py -q
```

没有 `flashinfer` 时，可先完成 CPU 参考实现并记录环境限制。

### H08 Attention 与 Kernel

完成 attention metadata、CPU reference 和至少一个可选 backend。自定义 kernel 必须先做 boundary-shape 与 PyTorch parity，再做 benchmark。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_gpu_kernel.py -q
```

没有 CUDA 时，提交 kernel 设计、reference 测试和待执行实验清单。

### H09 引擎与分布式

完成 greedy sampling、Engine forward、Graph runner 边界和 TP 信息接口。先在单卡跑通 prefill/decode，再做两 rank collective smoke。

交付：Engine 冒烟输出、stream/sync 说明、TP collective 测试记录。

### H10 服务链路

实现 server、tokenizer、detokenizer、LLM 门面和 shell。至少覆盖 `/v1/models`、chat completions、stream/non-stream、UTF-8 增量解码和客户端断开 abort。

验收：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_server.py -q
```

### H11 性能实验

实现 benchmark 计时和数据收集，用固定 workload 测量 TTFT、ITL、吞吐、显存。选择一个优化做单因素消融，并保留环境、命令和原始数据。

交付：一份可复现 benchmark 报告。

### H12 测试质量

检查每章是否覆盖正常路径、边界、非法输入和回归。补充至少一个资源释放测试、一个属性/随机测试，并记录非 GPU 覆盖率。

### H13 结课项目

按 [结课项目](13-capstone.md) 完成最小端到端路径。必做范围优先于高级优化；不能运行的 GPU 章节必须明确标记为环境未覆盖，而不是假装通过。

最终演示必须包含：架构图、请求时序、cache 命中、资源释放、测试结果和性能基线。

## 作业提交模板

每个 `Hxx` 建议在个人分支提交一条记录：

```text
作业：H05 KV Cache
实现范围：
设计决策：
测试命令与结果：
未覆盖风险：
下一步：
```

## 仓库与练习如何配合

默认命令只检查脚手架完整性和文档链接：

```bash
python -m pytest -x -q
```

章节练习默认跳过，因为初始仓库故意没有实现。开启练习后，失败是正常的起点：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_foundations.py -q
```

也可以只选择某个标记：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest -m "not gpu" -q
```

完整测试规则见 [测试手册](12-testing.md)。

## 如何阅读脚手架

- 模块与类的 docstring 说明设计意图。
- 参数名、返回类型和原始基类提示接口约束。
- `NotImplementedError` 标出必须由你填补的行为。
- [仓库与模块地图](03-code-map.md) 给出模块与章节的对应关系。
- git 历史中的原始实现只用于完成后做设计审阅，不建议学习时先打开。

## 课程地图

- [环境与硬件](01-environment.md)
- [基础训练](02-foundations.md)
- [请求与消息](04-core-and-messages.md)
- [KV Cache](05-kv-cache.md)
- [调度器](06-scheduler.md)
- [模型与层](07-models-and-layers.md)
- [Kernel 与 Attention](08-kernel-and-attention.md)
- [引擎与分布式](09-engine-and-distributed.md)
- [服务链路](10-serving.md)
- [性能实验](11-performance.md)
- [测试手册](12-testing.md)
- [仓库与模块地图](03-code-map.md)
- [结课项目](13-capstone.md)
- [教学使用说明](14-instructor-guide.md)
- [当前实现任务板](15-project-board.md)

## 判定“学会了”的标准

能背出公式不算完成。你需要能脱离源码解释：

1. 为什么 prefill 和 decode 的成本结构不同；
2. 为什么分页 KV cache 同时需要 page table、空闲页池和前缀索引；
3. 为什么 Radix Tree 的节点需要引用计数和淘汰时间戳；
4. 为什么 chunked prefill 需要跨调度轮次保存请求状态；
5. 为什么 overlap scheduling 必须区分 CPU metadata 与 GPU stream；
6. 为什么张量并行需要成对设计通信、切分和输出聚合；
7. 为什么自定义 kernel 必须先与 PyTorch 参考实现对齐；
8. 如何用 TTFT、ITL、吞吐和显存证明一次优化真的有效。

完成后进入 [结课项目](13-capstone.md)，用可复现证据而非主观感受验收。
