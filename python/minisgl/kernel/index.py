"""Teaching scaffold for minisgl.kernel.index.

Scaffold for minisgl.kernel.index.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _jit_index_module(
    element_size: int, *, num_splits: int = 1, config: KernelConfig = ...
) -> Module:
    """TODO: implement `_jit_index_module`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _jit_index_module()")


def indexing(
    weights: torch.Tensor,
    indices: torch.Tensor,
    *,
    output: torch.Tensor | None = None,
    vocab_range: Tuple[int, int] | None = None,
) -> torch.Tensor:
    """TODO: implement `indexing`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement indexing()")


DEFAULT_INDEX_KERNEL_CONFIG: Any = None
