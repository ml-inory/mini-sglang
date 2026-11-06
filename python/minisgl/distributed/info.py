"""Teaching scaffold for minisgl.distributed.info.

Scaffold for minisgl.distributed.info.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class DistributedInfo:
    """TODO: implement `DistributedInfo`."""

    def __post_init__(self):
        """TODO: implement `__post_init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __post_init__()")

    def is_primary(self) -> bool:
        """TODO: implement `is_primary`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_primary()")


def set_tp_info(rank: int, size: int) -> None:
    """TODO: implement `set_tp_info`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement set_tp_info()")


def get_tp_info() -> DistributedInfo:
    """TODO: implement `get_tp_info`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_tp_info()")


def try_get_tp_info() -> DistributedInfo | None:
    """TODO: implement `try_get_tp_info`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement try_get_tp_info()")


_TP_INFO: Any = None

__all__ = [
    "DistributedInfo",
    "set_tp_info",
    "get_tp_info",
    "try_get_tp_info",
]
