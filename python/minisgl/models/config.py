"""Teaching scaffold for minisgl.models.config.

Scaffold for minisgl.models.config.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class RotaryConfig:
    """TODO: implement `RotaryConfig`."""

    """TODO: replace this marker with the RotaryConfig implementation."""


class ModelConfig:
    """TODO: implement `ModelConfig`."""

    @property
    def is_moe(self) -> bool:
        """TODO: implement `is_moe`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_moe()")

    @classmethod
    def from_hf(cls, config: PretrainedConfig) -> ModelConfig:
        """TODO: implement `from_hf`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement from_hf()")
