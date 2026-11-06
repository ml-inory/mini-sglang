# 01 环境与硬件

## 本章作业 H01

建立三层环境中的至少第一层，并提交一份环境记录：Python 版本、安装命令、默认测试结果和可用的 GPU/CUDA 信息。高级硬件不可用时，明确写出跳过哪些实验。

验收命令：

```bash
python -m pytest -x -q
python -m minisgl --help
```

## 三层环境

本课程按三层组织环境，避免一开始就被 CUDA 工具链挡住。

### 第一层：CPU 教学环境

适合阅读、脚手架测试、纯 Python 数据结构、调度状态机、朴素缓存和序列化练习。

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
python -m pytest -x -q
```

第一层不要求安装 PyTorch，因为脚手架导入时会刻意避开重型运行时依赖。

### 第二层：PyTorch 与模型实验

适合实现 `Req` 的张量字段、RoPE、归一化、线性层、attention 参考实现和小模型加载。

```bash
python -m pip install -e ".[dev,model]"
```

模型章节应优先使用小模型和短序列。不要在调试 shape、dtype 或缓存索引时加载 70B 模型。建议把真实模型延迟到单层和引擎冒烟测试之后。

### 第三层：CUDA、分布式与性能实验

适合 FlashAttention、FlashInfer、TensorRT-LLM backend、自定义 kernel、CUDA Graph、NCCL 和多卡 TP。

```bash
python -m pip install -e ".[dev,model,serve,cuda]"
```

CUDA 依赖版本必须与实际驱动匹配。安装失败时先验证：

```bash
nvidia-smi
python -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available())"
```

如果 `torch.cuda.is_available()` 为 `False`，不要继续排查仓库代码，先修环境。

## 可选依赖组

| 依赖组 | 主要用途 | 是否 CPU 可学 |
|---|---|---|
| `dev` | pytest、覆盖率和静态检查 | 是 |
| `model` | PyTorch、Transformers、模型权重 | 部分 |
| `serve` | FastAPI、ZMQ、OpenAI client | 是 |
| `cuda` | FlashInfer、SGL kernel、TVM FFI | 否 |

## 环境变量

课程框架使用以下变量：

| 变量 | 作用 |
|---|---|
| `MINISGL_RUN_EXERCISES=1` | 启用车章练习 |
| `MINISGL_TEST_MODEL=/path/to/model` | 启用端到端模型测试 |

后续实现原项目功能时，还会遇到 `MINISGL_` 前缀的运行时变量。应在 `python/minisgl/env.py` 中集中解析，不要在业务模块里随意调用 `os.getenv`。

## 测试标记

```bash
# 仅脚手架自检
python -m pytest tests/smoke -q

# 启用车章练习，但排除 GPU
MINISGL_RUN_EXERCISES=1 python -m pytest -m "not gpu" -q

# 只跑 GPU kernel
MINISGL_RUN_EXERCISES=1 python -m pytest -m gpu -q

# 只做快速反馈
MINISGL_RUN_EXERCISES=1 python -m pytest -m "not slow" -q
```

## 目录与模型缓存

大模型、编译缓存和数据文件不要提交到 git。建议集中放在仓库外，或使用未跟踪目录：

- Hugging Face 模型缓存
- FlashInfer workspace
- TVM FFI 编译缓存
- benchmark trace

如果下载失败，先检查网络、代理和磁盘空间，再判断是否为代码问题。

## Docker

仓库自带的是 CPU 教学镜像，用于快速验证脚手架和测试框架。需要 GPU 时，自行基于匹配的 CUDA 镜像安装 `model`、`serve` 和 `cuda` 依赖组，并在 [性能实验](11-performance.md) 中记录镜像版本。

## 快速诊断表

| 症状 | 优先检查 |
|---|---|
| `import minisgl` 失败 | 当前目录、`pip install -e .`、`PYTHONPATH` |
| PyTorch 找不到 CUDA | 驱动、wheel 的 CUDA 版本、容器 GPU 透传 |
| FlashInfer 编译失败 | CUDA Toolkit、编译器、ABI、缓存权限 |
| 测试被跳过 | 是否设置 `MINISGL_RUN_EXERCISES=1` |
| 多卡进程卡住 | rank 数、端口、NCCL 网络、所有 rank 是否执行同一集合通信 |
| 显存增长不受控 | 先检查请求释放、缓存引用计数和 page table |

环境准备好后，从 [基础训练](02-foundations.md) 开始。
