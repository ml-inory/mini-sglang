<p align="center">
<img width="320" alt="Mini-SGLang logo" src="assets/logo.png">
</p>

# Mini-SGLang Teaching Repository

这是一个从 [mini-sglang](https://github.com/sgl-project/mini-sglang) 改造而来的教学仓。仓库保留完整的软件地图、模块边界、公开类与函数签名，但把具体实现替换成脚手架和 `NotImplementedError`。

目标不是让你一次读完所有代码，而是让你沿着一条可运行的测试路径，从请求数据模型一路实现到 KV Cache、Radix Cache、调度器、模型执行、分布式通信和 OpenAI 兼容服务。

## 当前状态

- 所有 Python 模块和 CUDA/C++ 原生源文件都保留在原路径。
- 脚手架模块不强制导入 `torch`、Transformers、CUDA 或其他重型依赖。
- 默认 `pytest` 只检查教学仓是否完整，不会因为尚未完成练习而失败。
- 章节练习默认跳过；设置 `MINISGL_RUN_EXERCISES=1` 后运行，才会进入 red-green 开发循环。
- `docs/` 提供总路线、模块地图、各子系统讲义、测试指南和结课标准。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"

# 检查教学仓自身
python -m pytest -x -q

# 开始第一章练习
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises -q

# 查看脚手架入口
python -m minisgl --help
```

高级章节需要 NVIDIA GPU、CUDA Toolkit、PyTorch 或对应模型运行时。请按 [环境与硬件](docs/01-environment.md) 的说明安装可选依赖，不要在本机环境不满足要求时强行运行 GPU 测试。

## 从这里开始

文档已经按数字编号，建议严格按顺序阅读：

1. [00 课程首页](docs/00-index.md)：学习路线与 H00-H13 作业总表。
2. [01 环境与硬件](docs/01-environment.md)：建立 CPU 基线，判断能否进入 GPU 章节。
3. [02 基础训练](docs/02-foundations.md)：完成 H02 基础工具。
4. [03 仓库与模块地图](docs/03-code-map.md)：完成 H03 架构图。
5. [04 请求与消息](docs/04-core-and-messages.md)：实现 Core 与消息协议。
6. [05 KV Cache](docs/05-kv-cache.md)：实现分页缓存与前缀复用。
7. [06 调度器](docs/06-scheduler.md)：实现 prefill、decode 和资源调度。
8. [07 模型与层](docs/07-models-and-layers.md)：实现 Transformer 组件。
9. [08 Kernel 与 Attention](docs/08-kernel-and-attention.md)：完成 reference 与可选 GPU 加速。
10. [09 引擎与分布式](docs/09-engine-and-distributed.md)：完成 Engine、采样和 TP。
11. [10 服务链路](docs/10-serving.md)：完成 tokenizer 与 OpenAI 兼容 API。
12. [11 性能实验](docs/11-performance.md)：完成 H11 benchmark 报告。
13. [12 测试手册](docs/12-testing.md)：完成 H12 测试质量检查。
14. [13 结课项目](docs/13-capstone.md)：完成 H13 端到端验收。

`14` 到 `17` 是教师参考、任务板、功能清单和系统结构资料，不需要插入主线顺序阅读。

## 重要原则

不要一次实现整个仓库。每一章只实现当前公开契约和对应测试，保持测试通过后再进入下一章。脚手架中的方法签名和文档是接口线索，不是可以直接复制的答案。

原始实现保存在 git 历史与 `main` 分支中。建议先独立实现，再把原仓库当作设计审阅材料，而不是参考答案。

## 许可证

本教学仓继承原项目的 MIT License，见 [LICENSE](LICENSE)。
