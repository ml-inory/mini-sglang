from __future__ import annotations

import importlib
import inspect
import subprocess
import sys
from pathlib import Path

import minisgl

ROOT = Path(__file__).resolve().parents[2]


def _module_names() -> list[str]:
    names: list[str] = []
    for path in sorted((ROOT / "python" / "minisgl").rglob("*.py")):
        relative = path.relative_to(ROOT / "python")
        parts = list(relative.with_suffix("").parts)
        if parts[-1] == "__init__":
            parts.pop()
        name = ".".join(parts)
        if not name.endswith(".__main__"):
            names.append(name)
    return names


def test_package_exposes_scaffold_marker() -> None:
    assert minisgl.__scaffold__ is True
    assert minisgl.__version__


def test_every_python_module_imports_without_heavy_dependencies() -> None:
    for name in _module_names():
        importlib.import_module(name)
    assert "torch" not in sys.modules
    assert "transformers" not in sys.modules


def test_public_contract_contains_teaching_stub() -> None:
    from minisgl.core import Req

    assert inspect.isclass(Req)
    with __import__("pytest").raises(NotImplementedError, match="Teaching scaffold"):
        Req.__post_init__(object())


def test_cli_help_points_learners_to_docs() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "minisgl", "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "teaching scaffold" in result.stdout.lower()
    assert "--model" in result.stdout
