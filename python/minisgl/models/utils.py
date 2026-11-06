"""Teaching scaffold for minisgl.models.utils.

Scaffold for minisgl.models.utils.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class GatedMLP:
    """TODO: implement `GatedMLP`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class MoEMLP:
    """TODO: implement `MoEMLP`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class RopeAttn:
    """TODO: implement `RopeAttn`. (original base: BaseOP)"""

    def __init__(
        self,
        config: ModelConfig,
        layer_id: int,
        *,
        has_attn_bias: bool = False,
        has_qk_norm: bool = False,
    ):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


__all__ = [
    "GatedMLP",
    "RopeAttn",
    "MoEMLP",
]
