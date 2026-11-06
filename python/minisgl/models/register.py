"""Teaching scaffold for minisgl.models.register.

Scaffold for minisgl.models.register.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def get_model_class(model_architecture: str, model_config: ModelConfig):
    """TODO: implement `get_model_class`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_model_class()")


_MODEL_REGISTRY: Any = None

__all__ = [
    "get_model_class",
]
