from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

REQUIRED_DOCS = {
    "index.md",
    "environment.md",
    "foundations.md",
    "core-and-messages.md",
    "kv-cache.md",
    "scheduler.md",
    "models-and-layers.md",
    "kernel-and-attention.md",
    "engine-and-distributed.md",
    "serving.md",
    "performance.md",
    "testing.md",
    "code-map.md",
    "capstone.md",
}


def test_required_curriculum_documents_exist() -> None:
    missing = sorted(name for name in REQUIRED_DOCS if not (DOCS / name).is_file())
    assert missing == []


def test_relative_markdown_links_resolve() -> None:
    broken: list[str] = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in DOCS.glob("*.md"):
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.exists():
                broken.append(f"{path.name} -> {target}")
    assert broken == []


def test_index_links_the_learning_path() -> None:
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    for name in REQUIRED_DOCS - {"index.md"}:
        assert name in index
