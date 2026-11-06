"""Teaching scaffold for minisgl.models.

Scaffold for minisgl.models.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from .base import BaseLLMModel
from .config import ModelConfig, RotaryConfig
from .register import get_model_class
from .weight import load_weight


def create_model(model_config: ModelConfig) -> BaseLLMModel:
    """TODO: implement `create_model`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_model()")


__all__ = [
    "create_model",
    "load_weight",
    "RotaryConfig",
]
