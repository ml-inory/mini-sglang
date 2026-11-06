"""Teaching scaffold for minisgl.attention.fi.

Scaffold for minisgl.attention.fi.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _next_power_of_2(n: int) -> int:
    """TODO: implement `_next_power_of_2`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _next_power_of_2()")


class FICaptureData:
    """TODO: implement `FICaptureData`. (original base: BaseCaptureData)"""

    @property
    def one_tensor(self) -> torch.Tensor:
        """TODO: implement `one_tensor`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement one_tensor()")

    @property
    def indices(self) -> torch.Tensor:
        """TODO: implement `indices`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement indices()")


class FIMetadata:
    """TODO: implement `FIMetadata`. (original base: BaseAttnMetadata)"""

    def __post_init__(self) -> None:
        """TODO: implement `__post_init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __post_init__()")

    def get_last_indices(self, bs: int) -> torch.Tensor:
        """TODO: implement `get_last_indices`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_last_indices()")


class FlashInferBackend:
    """TODO: implement `FlashInferBackend`. (original base: BaseAttnBackend)"""

    def __init__(self, config: ModelConfig) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def _initialize_metadata_once(self, metadata: FIMetadata) -> None:
        """TODO: implement `_initialize_metadata_once`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _initialize_metadata_once()")

    def _get_ones_cpu(self, bs: int) -> torch.Tensor:
        """TODO: implement `_get_ones_cpu`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _get_ones_cpu()")

    def forward(
        self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, layer_id: int, batch: Batch
    ) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")

    def prepare_metadata(self, batch: Batch) -> None:
        """TODO: implement `prepare_metadata`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare_metadata()")

    def init_capture_graph(self, max_seq_len: int, bs_list: List[int]) -> None:
        """TODO: implement `init_capture_graph`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement init_capture_graph()")

    def use_tensor_cores(self) -> bool:
        """TODO: implement `use_tensor_cores`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement use_tensor_cores()")

    def prepare_for_capture(self, batch: Batch) -> None:
        """TODO: implement `prepare_for_capture`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare_for_capture()")

    def prepare_for_replay(self, batch: Batch) -> None:
        """TODO: implement `prepare_for_replay`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare_for_replay()")


logger: Any = None
