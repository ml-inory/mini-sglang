# 12 测试手册

教学仓使用 pytest 构建三层测试。测试既验证你的实现，也承担“可执行规格”的作用。

## 本章作业 H12

审查前面所有章节的测试覆盖，补一个资源释放测试、一个随机/属性测试和一个错误路径测试。记录非 GPU 覆盖率，但不要用覆盖率替代状态机和资源不变量检查。

## 目录

```text
tests/
  conftest.py              # 练习开关、CUDA fixture
  smoke/                   # 教学仓自检，默认必须通过
  exercises/               # 章节实现练习，默认跳过
```

## 默认自检

```bash
python -m pytest -x -q
```

默认测试检查：

- 所有 Python 模块能在无 `torch`/CUDA 环境中导入；
- 所有原生源文件仍以教学脚手架存在；
- 课程文档齐全且相对链接有效；
- CLI 入口可运行；
- 脚手架方法确实未被提前填充答案。

如果你修改脚手架结构，记得同步更新 `tests/smoke/test_scaffold_inventory.py` 和 [仓库与模块地图](03-code-map.md)。

## 练习模式

```bash
# 全部练习
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises -q

# 命令行开关等价
python -m pytest --run-exercises tests/exercises -q

# 单章
MINISGL_RUN_EXERCISES=1 python -m pytest tests/exercises/test_foundations.py -vv

# 非 GPU
MINISGL_RUN_EXERCISES=1 python -m pytest -m "not gpu" -q

# GPU kernel
MINISGL_RUN_EXERCISES=1 python -m pytest -m gpu -q
```

## 推荐 red-green 循环

1. 只运行目标章节测试，确认失败原因是尚未实现；
2. 写一个最小实现；
3. 跑目标测试；
4. 加边界测试；
5. 跑全部非 GPU 练习；
6. 跑默认自检，确认没有破坏无依赖导入；
7. 记录设计理由和未覆盖风险。

## 可选依赖

练习按依赖逐层启用：

- 纯 Python：始终可运行；
- `torch`：由 `pytest.importorskip` 自动跳过缺失环境；
- `flashinfer`：仅 activation/attention 练习；
- `fastapi`：仅 server 练习；
- CUDA：使用 `gpu` 标记和 `require_cuda` fixture；
- 真实模型：只有设置 `MINISGL_TEST_MODEL` 才运行。

不要为了让测试“绿”而永久跳过缺少的依赖。应区分“环境未就绪”和“实现失败”。

## 新增练习测试

每个测试文件顶部添加：

```python
import pytest

pytestmark = pytest.mark.exercise
```

规则：

- 测试公开行为，不锁死无关内部实现；
- 使用固定 shape 和固定随机种子；
- 对边界条件参数化；
- GPU 测试同时标记 `gpu` 和 `slow`；
- 跨模块测试标记 `integration`；
- 失败消息包含实际 shape、dtype、device 或状态；
- 不包含完整参考实现，避免把测试变成答案。

## Fixture 使用

`require_cuda`：无 CUDA 时跳过。

```python
pytestmark = [pytest.mark.exercise, pytest.mark.gpu]

def test_kernel(require_cuda: None) -> None:
    ...
```

`simple_token_ids`：提供稳定的 8 个 token，适合 CPU 数据模型练习。

## 覆盖率

覆盖率用于发现遗漏，不是质量分数。优先覆盖状态转换、错误路径和资源释放。

```bash
MINISGL_RUN_EXERCISES=1 python -m pytest -m "not gpu" \
  --cov=minisgl --cov-report=term-missing
```

一个 90% 覆盖率但漏掉 cache unlock 的实现仍然可能严重错误。

## CI 建议

最小 CI 分三档：

1. 默认 smoke；
2. `not gpu` 练习；
3. 有专用 GPU runner 时运行 kernel 和 engine 集成。

CI 中缓存依赖编译，但不要在缓存 key 不匹配时复用旧 kernel。
