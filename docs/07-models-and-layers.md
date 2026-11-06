# 07 模型与层

本章把 Transformer 拆成可测试、可并行切分的组件。建议先实现无 TP 的 CPU 参考版本，再增加切分。

## 本章作业 H07

按 activation、RMSNorm、RoPE、linear、embedding、attention、minimal model 的顺序实现。每个算子先与 PyTorch 参考对齐，再实现 TP=2；至少保留一个固定输入/输出 golden case。

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_layers.py -q
```

## 配置与模型注册

`models/config.py` 描述 hidden size、层数、head 数、KV head 数、head dim、vocab size、RoPE 参数等。配置是各层 shape 的单一真相来源。

`models/register.py` 把 Hugging Face architecture 名称映射到本地模型类。注册表应允许：

- 明确注册；
- 查询未支持模型时报清晰错误；
- 同一个模型类按 config 支持变体；
- 避免 import 时加载所有重型模型。

`models/weight.py` 负责下载、加载、转换、切分和命名映射。建议先支持已转换为 safetensors 的小模型，再处理在线下载。

## 基础算子

### Linear

至少区分：

- 复制权重：每个 rank 持有完整权重；
- 列并行：输出维度切分；
- 行并行：输入维度切分，结果需要 all-reduce；
- fused QKV 和 output projection 的特殊切分。

先写一个单 rank 的矩阵乘测试，再推导每个 rank 的 slice 边界。最后测试 all-reduce 聚合结果与单 rank 全量计算一致。

### Embedding 与 LM Head

vocab 可能按 TP rank 切分。需要处理：

- 本 rank 的 vocab range；
- out-of-range token 的安全处理；
- logits gather；
- 采样只在 rank 0 或所有 rank 一致执行时的差异；
- padded token 不参与实际状态推进。

### RMSNorm

先写出 CPU 参考定义并验证 epsilon、dtype 和归一化轴。融合 residual 的版本必须说明输入是否原地修改。

### RoPE

Rotary Position Embedding 依赖位置、head dim 和 base frequency。测试时使用已计算好的小表，检查：

- cos/sin 排列；
- position offset；
- prefill 与 decode 的位置一致性；
- dtype 和 device；
- 缓存旋转表切换 device 时是否失效。

### Activation

`silu_and_mul`、`gelu_and_mul` 接收两路拼接输入，激活一路后与另一路逐元素相乘。先写 PyTorch 参考，再接 FlashInfer。

## Attention

`AttentionLayer` 负责选择 Q/K/V projection、RoPE、attention backend 和输出 projection。真正的 backend 只处理 attention 核心，不负责请求生命周期。

需要定义的输入：

- Q/K/V layout；
- token batch 与 page table；
- 因果 mask；
- 当前 batch 的 positions；
- 缓存写入位置；
- attention metadata。

CPU 参考路径可以用 dense causal attention 验证数学；分页路径再用同一组 Q/K/V 验证。

## MoE

`MoELayer` 至少包含 router、top-k 专家选择、token dispatch、专家 FFN 和加权合并。

练习顺序：

1. 无并行、无量化、确定性 router 的参考实现；
2. capacity factor 与溢出 token；
3. 专家并行时的 all-to-all；
4. fused kernel 与 Triton 路径；
5. 与稠密 MLP 在同权重条件下的数值对齐。

MoE 测试必须记录每个专家的 token 数。只看最终输出很难定位 dispatch 或合并错误。

## 支持的模型

`llama.py`、`mistral.py`、`qwen2.py`、`qwen3.py`、`qwen3_moe.py` 共享大部分 block 结构。不要复制粘贴五份实现后再分别修 bug。建议：

1. 提取通用 attention、MLP、norm 组合；
2. 用 config 表达模型差异；
3. 模型文件只保留结构装配和特殊行为；
4. 为每个模型保存最小 config 快照和层输出 golden data。

## 权重加载顺序

1. 只读列出 checkpoint tensor 名称和 shape；
2. 建立 checkpoint 名到本地参数名的显式映射；
3. 检查缺失和多余项；
4. 切分 TP 权重；
5. 加载到模块；
6. 用固定输入计算每层和整模型输出；
7. 最后才测试生成。

显式映射优于正则猜名字。shape 正确但转置错误，往往在完整推理时才会表现为乱码。

## 本章验收

- 所有 shape、dtype、device 有断言；
- 每个基础算子与 PyTorch 参考对齐；
- 单层 attention 和 MLP 有 golden 输出；
- TP 聚合结果与单 rank 结果在容差内一致；
- 至少一个小模型能完成一次 forward；
- 权重缺失、重复、shape mismatch 都有清晰报错。

下一章：[Kernel 与 Attention](08-kernel-and-attention.md)。
