# 基础训练

本章不是 Python 语法大全，而是列出实现 Mini-SGLang 时最容易“看得懂但写不对”的基础能力。建议用半天集中补齐，再进入核心模块。

## 1. 数据模型与不变量

LLM 服务里的 bug 很少来自一行复杂算法，更多来自状态不变量被破坏。例如：

- `input_ids` 在 CPU，模型输入在 GPU；
- `cached_len <= device_len <= max_device_len`；
- 已匹配前缀长度必须按 page size 对齐；
- 每个运行中的请求恰好占一张 table slot；
- 每个被引用的 cache page 不能被淘汰；
- 所有 TP rank 必须以相同顺序执行集合通信。

练习：为每个核心类写三栏表：字段、物理含义、不变量。

重点文件：`python/minisgl/core.py`、`python/minisgl/scheduler/table.py`、`python/minisgl/kvcache/base.py`。

## 2. dataclass、NamedTuple 与可变状态

课程中同时出现三种数据容器：

- `dataclass`：请求、配置、batch 等带可变字段的对象；
- `NamedTuple`：insert/match 返回值等轻量不可变结果；
- 普通 class：有生命周期或资源的 manager、engine、server。

学习要点：

1. `eq=False` 何时必要？如果请求作为集合元素，但内容持续变化，会发生什么？
2. 为什么 cache handle 的相等性应关注节点身份，而不是动态长度文本？
3. 哪些对象可以跨进程序列化，哪些对象包含不可搬运的资源？

练习：阅读 `Req`、`Batch`、`SchedulerConfig` 的签名，先写字段不变量测试，再实现类。

## 3. 类型与边界

PyTorch 代码必须同时关注四个属性：

- shape：每个维度代表什么；
- dtype：int32、int64、float16、bfloat16 是否会隐式转换；
- device：CPU、GPU、pinned CPU；
- contiguity / stride：kernel 是否假设内存连续。

常见错误是“shape 对但语义错”。例如 page table 中一个元素代表 token 对应的物理 KV 位置，而 page 列表中的一个元素代表页起始位置。

练习：遇到 `[B, S, H, D]` 张量时，强制写出 `B/S/H/D` 含义，不允许只写“tensor”。

## 4. 对齐与分页数学

设 `L` 为 token 长度、`P` 为 page size：

- 需要页数：`ceil(L / P)`；
- 前缀可插入长度：`floor(L / P) * P`；
- 某 token 所在页：`token_index // P`；
- 页起点展开为 token 起点：`page_index * P`。

实现前先手算 `L=10, P=4` 的所有边界。再思考长度恰好为 8、9 的情况，最容易出现 off-by-one。

## 5. 上下文管理器与资源释放

以下资源都需要确定性释放或恢复：

- 请求占用的 table slot；
- KV cache handle 的 lock；
- 张量 stream；
- FastAPI streaming generator；
- multiprocessing worker；
- 分布式 process group。

重点理解 `Context.forward_batch` 的作用。全局上下文只在单次 forward 中有效；嵌套进入应被明确拒绝，异常退出也必须清空。

## 6. 并发、消息与背压

系统同时存在四类“并发”：

1. Python 异步任务：API 请求和流式返回；
2. 多进程：API、tokenizer、scheduler、detokenizer；
3. 多个 CUDA stream：调度 metadata 与计算重叠；
4. 多卡 process group：TP rank 间集合通信。

学习重点不是会用线程池，而是明确“谁拥有状态”。scheduler 线程/进程拥有请求状态；API 进程只持有 uid 和回复队列。不要让两个进程同时修改同一个 `Req`。

## 7. PyTorch 必需知识

至少掌握：

- `torch.inference_mode()`；
- `pin_memory()` 与异步 H2D copy；
- `torch.cuda.Stream` 和 `wait_stream`；
- `torch.distributed` 的 rank/world size；
- `all_reduce`、`all_gather`、broadcast；
- dtype 与 device 转换；
- `torch.nn.functional` 中的参考算子。

优先实现 CPU 参考函数，例如 `silu(x) * gate`、softmax attention 和 RMSNorm。GPU kernel 的价值来自性能，不来自替代数学定义。

## 8. 测试基本功

每个实现至少写四类测试：

1. 正常路径；
2. 边界值：0、1、恰好一页、跨页；
3. 非法输入：长度越界、重复释放、超过容量；
4. 回归：先失败、修复后通过，并保留失败原因。

示例命令：

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_foundations.py -vv
```

基础练习通过后，阅读 [请求与消息](core-and-messages.md)。
