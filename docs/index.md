# Mini-SGLang 教学仓课程首页

这个仓库不是一份可以直接部署的推理系统，而是一张可以动手重建的工程地图。原项目中的每个模块路径都被保留，类和函数签名作为接口线索存在，函数体统一等待你实现。

学习目标不是“背完所有源码”，而是建立一条完整因果链：

> 文本变成 token，token 变成请求，请求被调度成 batch，batch 通过模型和 attention 计算，KV 被缓存和复用，token 再流回用户。

## 先读这三条规则

1. **每次只改变一个可解释的层次。** 先让数据结构和纯 Python 契约通过测试，再接入 PyTorch，再考虑 CUDA。
2. **测试先于优化。** 没有正确性基线和可复现测量时，不比较吞吐、显存或延迟。
3. **硬件能力不是学习前提。** CPU 主线必须可完成；GPU、分布式和原生 kernel 是进阶模块，可以按硬件条件逐项解锁。

## 推荐学习路径

| 阶段 | 文档 | 你要回答的问题 | 完成信号 |
|---|---|---|---|
| 0 | [环境与硬件](environment.md) | 我的环境能学到哪一章？ | 默认测试通过 |
| 1 | [基础训练](foundations.md) | 张量、类型、并发和测试的最小知识是什么？ | 基础练习通过 |
| 2 | [仓库与模块地图](code-map.md) | 每个目录负责什么？ | 能画出模块依赖 |
| 3 | [请求与消息](core-and-messages.md) | 一个生成请求如何表示和传输？ | Core 与消息练习通过 |
| 4 | [KV Cache](kv-cache.md) | 为什么缓存 K/V？前缀复用什么？ | Naive/Radix 缓存练习通过 |
| 5 | [调度器](scheduler.md) | prefill、decode、分块和资源约束如何协同？ | 调度状态机通过 |
| 6 | [模型与层](models-and-layers.md) | Transformer 如何被模块化并并行切分？ | 单层参考计算对齐 |
| 7 | [Attention 与 Kernel](kernel-and-attention.md) | attention 后端和自定义 kernel 怎样接入？ | CPU 参考通过后再上 GPU |
| 8 | [引擎与分布式](engine-and-distributed.md) | 计算、图重放、TP 和调度如何组合？ | 单卡引擎冒烟 |
| 9 | [服务链路](serving.md) | OpenAI 兼容 API 如何处理流式请求？ | API 集成测试通过 |
| 10 | [性能实验](performance.md) | 正确之后怎样证明优化有效？ | 有基线、假设和回归阈值 |
| 11 | [结课项目](capstone.md) | 能否从零跑通一个受控模型？ | 完整验收表通过 |

建议每周完成一个阶段，并保留这一节奏：阅读契约 -> 手写状态图 -> 实现最小版本 -> 运行定向测试 -> 补充边界测试 -> 记录下一步。

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

完整测试规则见 [测试手册](testing.md)。

## 如何阅读脚手架

- 模块与类的 docstring 说明设计意图。
- 参数名、返回类型和原始基类提示接口约束。
- `NotImplementedError` 标出必须由你填补的行为。
- [仓库与模块地图](code-map.md) 给出模块与章节的对应关系。
- git 历史中的原始实现只用于完成后做设计审阅，不建议学习时先打开。

## 课程地图

- [环境与硬件](environment.md)
- [基础训练](foundations.md)
- [请求与消息](core-and-messages.md)
- [KV Cache](kv-cache.md)
- [调度器](scheduler.md)
- [模型与层](models-and-layers.md)
- [Kernel 与 Attention](kernel-and-attention.md)
- [引擎与分布式](engine-and-distributed.md)
- [服务链路](serving.md)
- [性能实验](performance.md)
- [测试手册](testing.md)
- [仓库与模块地图](code-map.md)
- [结课项目](capstone.md)
- [教学使用说明](instructor-guide.md)
- [当前实现任务板](project-board.md)

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

完成后进入 [结课项目](capstone.md)，用可复现证据而非主观感受验收。
