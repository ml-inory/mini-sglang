"""Teaching scaffold for minisgl.layers.attention.

Scaffold for minisgl.layers.attention.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class AttentionLayer:
    """TODO: implement `AttentionLayer`. (original base: StateLessOP)"""

    def __init__(
        self,
        layer_id: int,
        num_qo_heads: int,
        num_kv_heads: int,
        head_dim: int,
        rotary_config: RotaryConfig,
        q_norm: RMSNorm | None = None,
        k_norm: RMSNorm | None = None,
    ):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, qkv: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
