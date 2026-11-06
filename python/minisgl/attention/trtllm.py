"""Teaching scaffold for minisgl.attention.trtllm.

Scaffold for minisgl.attention.trtllm.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class TRTLLMCaptureData:
    """TODO: implement `TRTLLMCaptureData`. (original base: BaseCaptureData)"""

    """TODO: replace this marker with the TRTLLMCaptureData implementation."""


class TRTLLMMetadata:
    """TODO: implement `TRTLLMMetadata`. (original base: BaseAttnMetadata)"""

    def get_last_indices(self, bs: int) -> torch.Tensor:
        """TODO: implement `get_last_indices`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_last_indices()")


class TensorRTLLMBackend:
    """TODO: implement `TensorRTLLMBackend`. (original base: BaseAttnBackend)"""

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
