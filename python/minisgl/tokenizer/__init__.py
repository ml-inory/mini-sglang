"""Teaching scaffold for minisgl.tokenizer.

Scaffold for minisgl.tokenizer.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from .server import tokenize_worker

__all__ = [
    "tokenize_worker",
]
