"""Teaching scaffold for minisgl.moe.base.

Scaffold for minisgl.moe.base.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseMoeBackend:
    """TODO: implement `BaseMoeBackend`. (original base: ABC)"""

    def forward(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
        gating_output: torch.Tensor,
        topk: int,
        renormalize: bool,
        activation: str,
        apply_router_weight_on_input: bool,
    ) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
