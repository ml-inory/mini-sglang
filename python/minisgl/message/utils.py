"""Teaching scaffold for minisgl.message.utils.

Scaffold for minisgl.message.utils.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _serialize_any(value: Any) -> Any:
    """TODO: implement `_serialize_any`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _serialize_any()")


def serialize_type(self) -> Dict:
    """TODO: implement `serialize_type`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement serialize_type()")


def _deserialize_any(cls_map: Dict[str, Type], data: Any) -> Any:
    """TODO: implement `_deserialize_any`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _deserialize_any()")


def deserialize_type(cls_map: Dict[str, Type], data: Dict) -> Any:
    """TODO: implement `deserialize_type`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement deserialize_type()")
