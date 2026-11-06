"""Teaching scaffold for minisgl.layers.activation.

Scaffold for minisgl.layers.activation.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def silu_and_mul(x: torch.Tensor, out: torch.Tensor | None = None):
    """TODO: implement `silu_and_mul`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement silu_and_mul()")


def gelu_and_mul(x: torch.Tensor, out: torch.Tensor | None = None):
    """TODO: implement `gelu_and_mul`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement gelu_and_mul()")


__all__ = [
    "silu_and_mul",
    "gelu_and_mul",
]
