# 当前实现任务板

GitHub issue 在本仓库关闭，因此教学改造使用本文件作为本地可审计任务板。

## 本地任务 001：完成教学脚手架

目标：保留全部 mini-sglang 模块路径，把实现替换成可学习脚手架，并加入 pytest 与课程文档。

验收：

- [x] `python/minisgl` 下所有 Python 模块保留并转换为脚手架；
- [x] CUDA/C++ 原生源文件保留为 TODO 脚手架；
- [x] 默认导入不依赖 PyTorch、CUDA 或 Transformers；
- [x] 默认 pytest 只验证脚手架，不因未实现练习失败；
- [x] 练习测试可通过 `MINISGL_RUN_EXERCISES=1` 或 `--run-exercises` 启用；
- [x] 环境、基础、core、cache、scheduler、model、kernel、engine、serving、performance、testing、capstone 文档已建立；
- [x] 总课程首页与完整模块地图已建立。

学习者后续可在自己的分支把本章任务拆成 issue：

```text
feat(core): implement request state invariants
feat(cache): implement radix prefix matching
feat(scheduler): implement chunked prefill
feat(server): implement streaming chat completions
```

每个任务至少包含：目标、非目标、验收测试、资源风险和一个可回退边界。
