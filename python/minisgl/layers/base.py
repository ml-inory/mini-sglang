"""Teaching scaffold for minisgl.layers.base.

Scaffold for minisgl.layers.base.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _concat_prefix(prefix: str, name: str) -> str:
    """TODO: implement `_concat_prefix`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _concat_prefix()")


class BaseOP:
    """TODO: implement `BaseOP`."""

    def forward(self, *args: Any, **kwargs: Any) -> Any:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")

    def state_dict(self, *, prefix: str = "", result: _STATE_DICT | None = None) -> _STATE_DICT:
        """TODO: implement `state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement state_dict()")

    def load_state_dict(
        self, state_dict: _STATE_DICT, *, prefix: str = "", _internal: bool = False
    ) -> None:
        """TODO: implement `load_state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement load_state_dict()")


class StateLessOP:
    """TODO: implement `StateLessOP`. (original base: BaseOP)"""

    def __init__(self):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def load_state_dict(
        self, state_dict: _STATE_DICT, *, prefix: str = "", _internal: bool = False
    ) -> None:
        """TODO: implement `load_state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement load_state_dict()")

    def state_dict(self, *, prefix: str = "", result: _STATE_DICT | None = None) -> _STATE_DICT:
        """TODO: implement `state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement state_dict()")


class OPList:
    """TODO: implement `OPList`. (original base: BaseOP, Generic[T])"""

    def __init__(self, ops: List[T]):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def state_dict(self, *, prefix: str = "", result: _STATE_DICT | None = None) -> _STATE_DICT:
        """TODO: implement `state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement state_dict()")

    def load_state_dict(
        self, state_dict: _STATE_DICT, *, prefix: str = "", _internal: bool = False
    ) -> None:
        """TODO: implement `load_state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement load_state_dict()")


_STATE_DICT: Any = None
T: Any = None
