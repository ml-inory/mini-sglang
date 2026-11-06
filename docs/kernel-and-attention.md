# Kernel 与 Attention 后端

这一章处理“性能相关但数学不变”的实现。原则是先参考、后向量化、再 kernel，最后才比较性能。

## Attention Backend 统一契约

课程中的 `BaseAttnBackend` 应隐藏不同厂商 API 的差异。上层调度器只准备统一 metadata，backend 负责：

- 读取 Q、K、V 和 paged KV cache；
- 处理因果 mask；
- 执行 prefill 或 decode attention；
- 返回与 batch 对齐的输出；
- 明确临时 workspace 的生命周期。

先定义错误：

- page size 不支持；
- head dim 不支持；
- prefill/decode metadata 混用；
- device 或 dtype 不一致；
- cache 位置越界。

## 三种 backend

### FlashAttention (`fa.py`)

通常用于 prefill 和部分 decode。重点理解可变序列长度、causal mask 和 head layout。

### FlashInfer (`fi.py`)

强调 paged decode 和 metadata 构造。要区分 logical token position、page index 和 slot index。

### TensorRT-LLM (`trtllm.py`)

通常对 page size 和形状有更严格约束。backend 可以在初始化时覆盖默认 page size，但必须把最终配置回报给 cache 与 scheduler。

### Hybrid Backend

prefill 与 decode 可选择不同实现。聚合 backend 必须按 phase 路由，任何一侧失败都应报出 phase 和 backend 名称。

## 自定义 Kernel 分层

### CUDA 与 C++

`kernel/csrc` 保留：

- native binding；
- tensor 辅助；
- NCCL 包装；
- JIT store/index；
- radix compare；
- warp 和通用工具头文件。

实现顺序：

1. 写 PyTorch reference；
2. 写小型 CPU/C++ unit；
3. 写单 block kernel；
4. 对齐随机 shape；
5. 测试边界 shape 和对齐；
6. 测 launch overhead；
7. 再优化 memory coalescing。

### Triton

`kernel/triton/fused_moe.py` 适合研究 fused MoE。必须测试：

- 不同 token 数；
- 不同 top-k；
- 空专家；
- 非整齐的 tile 边界；
- float16/bfloat16 容差；
- 确定性。

### TVM FFI

JIT 编译需要稳定缓存路径和编译错误回传。不要在 import 时编译所有 kernel。第一次调用时编译可以接受，但必须展示编译状态和缓存命中。

### PyNCCL

`pynccl.py` 和 native 头文件用于 rank 间通信。集合通信测试必须启动多个进程，不能在一个进程里模拟两个 rank。所有 rank 必须按同样顺序调用同样大小、同样 dtype 的 collective。

## 正确性测试模板

```text
固定随机种子
生成覆盖边界形状的输入
运行 reference
运行 candidate
比较 max abs error / relative error / exact token indices
保存首个 mismatch 的 shape、index 和 dtype
```

只有通过 same-shape 和 boundary-shape 后，才测性能。

## 性能记录

每个 kernel 至少报告：

- shape 与 dtype；
- warmup 次数；
- repeat 次数与统计方法；
- 中位数和 P95；
- reference 与 candidate；
- 峰值临时内存；
- 编译时间是否计入。

## 安全边界

- 越界访问在 GPU 上可能静默破坏其他 buffer；
- 未同步读取会让 benchmark 结果失真；
- 非确定性 atomic 顺序会破坏 greedy 回归；
- JIT 编译不可信代码前必须检查来源；
- 多卡失败时确保所有 rank 最终退出，避免残留进程。

没有 GPU 时，应完成参考实现、metadata 设计、伪 kernel 测试和性能实验方案，而不是把无法运行伪装成通过。

## 本章验收

- attention backend 的 phase 路由清晰；
- CPU reference 覆盖 prefill 和 decode；
- page size 约束有显式检查；
- kernel 边界 shape 测试通过；
- GPU benchmark 有同步与 warmup；
- PyNCCL 多进程测试可重复；
- 性能结论包含误差范围和环境。

下一章：[引擎与分布式](engine-and-distributed.md)。
