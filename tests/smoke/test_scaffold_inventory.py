from __future__ import annotations

import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "python" / "minisgl"


EXPECTED_SUBSYSTEMS = {
    "attention",
    "benchmark",
    "distributed",
    "engine",
    "kernel",
    "kvcache",
    "layers",
    "llm",
    "message",
    "models",
    "moe",
    "scheduler",
    "server",
    "tokenizer",
    "utils",
}


def test_all_subsystems_have_scaffold_files() -> None:
    present = {path.name for path in PACKAGE.iterdir() if path.is_dir()}
    assert EXPECTED_SUBSYSTEMS <= present


@pytest.mark.parametrize(
    "relative_path",
    [
        "kernel/csrc/jit/index.cu",
        "kernel/csrc/jit/store.cu",
        "kernel/csrc/src/pynccl.cu",
        "kernel/csrc/src/radix.cpp",
        "kernel/csrc/src/tensor.cpp",
        "kernel/csrc/include/minisgl/nccl227.h",
    ],
)
def test_native_sources_remain_as_scaffolds(relative_path: str) -> None:
    path = PACKAGE / relative_path
    assert path.exists()
    assert "Teaching scaffold" in path.read_text(encoding="utf-8")
    assert "TODO" in path.read_text(encoding="utf-8")


def test_python_scaffolds_do_not_import_runtime_libraries_at_module_scope() -> None:
    forbidden = {"torch", "transformers", "flashinfer", "triton", "fastapi"}
    violations: list[str] = []
    for path in PACKAGE.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.Import):
                names = {alias.name.split(".", 1)[0] for alias in node.names}
            elif isinstance(node, ast.ImportFrom):
                names = {(node.module or "").split(".", 1)[0]}
            else:
                continue
            if names & forbidden:
                violations.append(str(path.relative_to(ROOT)))
    assert violations == []
