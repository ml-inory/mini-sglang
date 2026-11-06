"""Teaching scaffold for minisgl.utils.logger.

Scaffold for minisgl.utils.logger.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def init_logger(
    name: str,
    suffix: str = "",
    *,
    strip_file: bool = True,
    level: str | None = None,
    use_pid: bool | None = None,
    use_tp_rank: bool | None = None,
):
    """Initialize the logger for the module with colors and pretty formatting."""
    raise NotImplementedError("Teaching scaffold: implement init_logger()")


_LOG_LEVEL: Any = None
