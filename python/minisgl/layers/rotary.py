"""Teaching scaffold for minisgl.layers.rotary.

Scaffold for minisgl.layers.rotary.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class RotaryEmbedding:
    """TODO: implement `RotaryEmbedding`. (original base: StateLessOP)"""

    def __init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: float,
        post_process: None | Callable[[torch.Tensor], torch.Tensor] = None,
    ) -> None:
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, positions: torch.Tensor, query: torch.Tensor, key: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


def _get_rope(
    head_dim: int,
    rotary_dim: int,
    max_position: int,
    base: float,
    rope_scaling: Dict[str, Any] | None = None,
) -> RotaryEmbedding:
    """TODO: implement `_get_rope`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _get_rope()")


def set_rope_device(device: torch.device):
    """TODO: implement `set_rope_device`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement set_rope_device()")


def get_rope(
    head_dim: int,
    rotary_dim: int,
    max_position: int,
    base: float,
    rope_scaling: Tuple[Tuple[str, Any], ...] | None = None,
) -> RotaryEmbedding:
    """TODO: implement `get_rope`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_rope()")


_ROPE_DEVICE: Any = None

__all__ = [
    "get_rope",
    "RotaryEmbedding",
    "set_rope_device",
]
