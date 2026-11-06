"""Teaching scaffold for minisgl.scheduler.

Scaffold for minisgl.scheduler.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from .config import SchedulerConfig
from .scheduler import Scheduler

__all__ = [
    "Scheduler",
    "SchedulerConfig",
]
