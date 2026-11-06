"""Teaching scaffold for minisgl.moe.

Scaffold for minisgl.moe.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from minisgl.utils import Registry, init_logger

from .base import BaseMoeBackend


class MoeBackendCreator:
    """TODO: implement `MoeBackendCreator`. (original base: Protocol)"""

    def __call__(self) -> BaseMoeBackend:
        """TODO: implement `__call__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __call__()")


def create_fused_moe_backend():
    """TODO: implement `create_fused_moe_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_fused_moe_backend()")


def create_moe_backend(backend: str) -> BaseMoeBackend:
    """TODO: implement `create_moe_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_moe_backend()")


logger: Any = None
SUPPORTED_MOE_BACKENDS: Any = None

__all__ = [
    "BaseMoeBackend",
    "create_moe_backend",
    "SUPPORTED_MOE_BACKENDS",
]
