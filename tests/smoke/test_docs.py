from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

REQUIRED_DOCS = {
    "00-index.md",
    "01-environment.md",
    "02-foundations.md",
    "04-core-and-messages.md",
    "05-kv-cache.md",
    "06-scheduler.md",
    "07-models-and-layers.md",
    "08-kernel-and-attention.md",
    "09-engine-and-distributed.md",
    "10-serving.md",
    "11-performance.md",
    "12-testing.md",
    "03-code-map.md",
    "13-capstone.md",
}

MAIN_CURRICULUM = [f"{number:02d}-" for number in range(14)]


def test_required_curriculum_documents_exist() -> None:
    missing = sorted(name for name in REQUIRED_DOCS if not (DOCS / name).is_file())
    assert missing == []


def test_all_documents_have_numeric_order_prefixes() -> None:
    invalid = [
        path.name
        for path in DOCS.glob("*.md")
        if not re.fullmatch(r"\d{2}-[a-z0-9-]+\.md", path.name)
    ]
    assert invalid == []


def test_main_curriculum_numbering_is_contiguous() -> None:
    actual = sorted(name[:2] for name in REQUIRED_DOCS)
    expected = [f"{number:02d}" for number in range(14)]
    assert actual == expected
    assert all(any(name.startswith(prefix) for name in REQUIRED_DOCS) for prefix in MAIN_CURRICULUM)


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
    index = (DOCS / "00-index.md").read_text(encoding="utf-8")
    for name in REQUIRED_DOCS - {"00-index.md"}:
        assert name in index
    for number in range(14):
        assert f"H{number:02d}" in index
