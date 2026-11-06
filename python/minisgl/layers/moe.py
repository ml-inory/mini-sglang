"""Teaching scaffold for minisgl.layers.moe.

Scaffold for minisgl.layers.moe.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class MoELayer:
    """TODO: implement `MoELayer`. (original base: BaseOP)"""

    def __init__(
        self,
        num_experts: int,
        top_k: int,
        hidden_size: int,
        intermediate_size: int,
        renormalize: bool = True,
        activation: str = "silu",
        apply_router_weight_on_input: bool = False,
    ):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, hidden_states: torch.Tensor, router_logits: torch.Tensor):
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
