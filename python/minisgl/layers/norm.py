"""Teaching scaffold for minisgl.layers.norm.

Scaffold for minisgl.layers.norm.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class RMSNorm:
    """TODO: implement `RMSNorm`. (original base: BaseOP)"""

    def __init__(self, size: int, eps: float) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")

    def forward_inplace(self, x: torch.Tensor) -> None:
        """TODO: implement `forward_inplace`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward_inplace()")


class RMSNormFused:
    """TODO: implement `RMSNormFused`. (original base: BaseOP)"""

    def __init__(self, size: int, eps: float) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, x: torch.Tensor, residual: torch.Tensor | None = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
