"""Teaching scaffold for minisgl.kernel.store.

Scaffold for minisgl.kernel.store.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _jit_store_module(element_size: int, *, config: KernelConfig = ...) -> Module:
    """TODO: implement `_jit_store_module`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _jit_store_module()")


def store_cache(
    k_cache: torch.Tensor,
    v_cache: torch.Tensor,
    indices: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
) -> None:
    """TODO: implement `store_cache`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement store_cache()")


DEFAULT_INDEX_KERNEL_CONFIG: Any = None
