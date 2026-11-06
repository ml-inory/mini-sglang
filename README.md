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

高级章节需要 NVIDIA GPU、CUDA Toolkit、PyTorch 或对应模型运行时。请按 [环境与硬件](docs/environment.md) 的说明安装可选依赖，不要在本机环境不满足要求时强行运行 GPU 测试。

## 从这里开始

1. 阅读 [课程首页](docs/index.md)，了解推荐顺序和学习方法。
2. 阅读 [仓库与模块地图](docs/code-map.md)，在源码目录中标出每个子系统的位置。
3. 完成 [基础训练](docs/foundations.md)，补齐 Python、张量、并发和测试基础。
4. 按章节实现 [核心请求模型](docs/core-and-messages.md)、[KV Cache](docs/kv-cache.md) 和 [调度器](docs/scheduler.md)。
5. 继续完成 [模型与层](docs/models-and-layers.md)、[引擎与分布式](docs/engine-and-distributed.md)、[服务链路](docs/serving.md) 和 [性能实验](docs/performance.md)。
6. 用 [结课项目](docs/capstone.md) 做一次端到端验收。

## 重要原则

不要一次实现整个仓库。每一章只实现当前公开契约和对应测试，保持测试通过后再进入下一章。脚手架中的方法签名和文档是接口线索，不是可以直接复制的答案。

原始实现保存在 git 历史与 `main` 分支中。建议先独立实现，再把原仓库当作设计审阅材料，而不是参考答案。

## 许可证

本教学仓继承原项目的 MIT License，见 [LICENSE](LICENSE)。
