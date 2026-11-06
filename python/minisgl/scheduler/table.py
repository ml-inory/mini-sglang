"""Teaching scaffold for minisgl.scheduler.table.

Scaffold for minisgl.scheduler.table.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class TableManager:
    """TODO: implement `TableManager`."""

    def __init__(self, max_running_reqs: int, page_table: torch.Tensor) -> None:
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    @property
    def available_size(self) -> int:
        """TODO: implement `available_size`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement available_size()")

    def allocate(self) -> int:
        """TODO: implement `allocate`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement allocate()")

    def free(self, slot: int) -> None:
        """TODO: implement `free`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement free()")
