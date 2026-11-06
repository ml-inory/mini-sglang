"""Teaching scaffold for minisgl.attention.fa.

Scaffold for minisgl.attention.fa.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class FACaptureData:
    """TODO: implement `FACaptureData`. (original base: BaseCaptureData)"""

    """TODO: replace this marker with the FACaptureData implementation."""


class FAMetadata:
    """TODO: implement `FAMetadata`. (original base: BaseAttnMetadata)"""

    def get_last_indices(self, bs: int) -> torch.Tensor:
        """TODO: implement `get_last_indices`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_last_indices()")


class FlashAttentionBackend:
    """TODO: implement `FlashAttentionBackend`. (original base: BaseAttnBackend)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, layer_id: int, batch: Batch
    ) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")

    def prepare_metadata(self, batch: Batch) -> None:
        """TODO: implement `prepare_metadata`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare_metadata()")

    def init_capture_graph(self, max_seq_len: int, bs_list: List[int]) -> None:
        """TODO: implement `init_capture_graph`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement init_capture_graph()")

    def prepare_for_capture(self, batch: Batch) -> None:
        """TODO: implement `prepare_for_capture`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare_for_capture()")

    def prepare_for_replay(self, batch: Batch) -> None:
        """TODO: implement `prepare_for_replay`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare_for_replay()")


def _fa_sgl_impl(
    q: torch.Tensor,
    k_cache: torch.Tensor,
    v_cache: torch.Tensor,
    page_table: torch.Tensor,
    cache_seqlens: torch.Tensor,
    cu_seqlens_q: torch.Tensor,
    cu_seqlens_k: torch.Tensor,
    max_seqlen_q: int,
    softmax_scale: float,
    version: int,
    sm_margin: int = 0,
    window_size: Tuple[int, int] = ...,
    softcap: float = 0.0,
    num_splits: int = 0,
    pack_gqa: bool | None = None,
    causal: bool = True,
) -> torch.Tensor:
    """TODO: implement `_fa_sgl_impl`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _fa_sgl_impl()")
