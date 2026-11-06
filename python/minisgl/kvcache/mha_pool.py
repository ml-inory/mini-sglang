"""Teaching scaffold for minisgl.kvcache.mha_pool.

Scaffold for minisgl.kvcache.mha_pool.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class MHAKVCache:
    """Base class for key-value caches.
    This class defines the interface for key-value caches used in LLMs.
    """

    def __init__(
        self,
        num_kv_heads: int,
        num_layers: int,
        head_dim: int,
        num_pages: int,
        page_size: int,
        dtype: torch.dtype,
        device: torch.device,
    ) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def k_cache(self, index: int) -> torch.Tensor:
        """TODO: implement `k_cache`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement k_cache()")

    def v_cache(self, index: int) -> torch.Tensor:
        """TODO: implement `v_cache`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement v_cache()")

    def store_kv(
        self, k: torch.Tensor, v: torch.Tensor, out_loc: torch.Tensor, layer_id: int
    ) -> None:
        """TODO: implement `store_kv`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement store_kv()")

    @property
    def device(self) -> torch.device:
        """TODO: implement `device`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement device()")

    @property
    def dtype(self) -> torch.dtype:
        """TODO: implement `dtype`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement dtype()")

    @property
    def num_layers(self) -> int:
        """TODO: implement `num_layers`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement num_layers()")
