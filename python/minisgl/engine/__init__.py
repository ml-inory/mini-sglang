"""Teaching scaffold for minisgl.engine.

Scaffold for minisgl.engine.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from .config import EngineConfig
from .engine import Engine, ForwardOutput
from .sample import BatchSamplingArgs

__all__ = [
    "Engine",
    "EngineConfig",
    "ForwardOutput",
    "BatchSamplingArgs",
]
