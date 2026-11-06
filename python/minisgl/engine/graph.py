"""Teaching scaffold for minisgl.engine.graph.

Scaffold for minisgl.engine.graph.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class GraphCaptureBuffer:
    """TODO: implement `GraphCaptureBuffer`."""

    @classmethod
    def init(cls, bs: int, vocab_size: int, device: torch.device) -> GraphCaptureBuffer:
        """TODO: implement `init`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement init()")

    def set_batch(self, batch: Batch) -> None:
        """TODO: implement `set_batch`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement set_batch()")

    def copy_from(self, batch: Batch) -> None:
        """TODO: implement `copy_from`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement copy_from()")


def _determine_cuda_graph_bs(
    cuda_graph_bs: List[int] | None, cuda_graph_max_bs: int | None, free_memory: int
) -> List[int]:
    """TODO: implement `_determine_cuda_graph_bs`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _determine_cuda_graph_bs()")


def mem_GB(size: int) -> str:
    """TODO: implement `mem_GB`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement mem_GB()")


def get_free_memory(device: torch.device) -> int:
    """TODO: implement `get_free_memory`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_free_memory()")


class GraphRunner:
    """TODO: implement `GraphRunner`."""

    def __init__(
        self,
        stream: torch.cuda.Stream,
        device: torch.device,
        model: BaseLLMModel,
        attn_backend: BaseAttnBackend,
        cuda_graph_bs: List[int] | None,
        cuda_graph_max_bs: int | None,
        free_memory: int,
        max_seq_len: int,
        vocab_size: int,
        dummy_req: Req,
    ) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def _capture_graphs(self, max_seq_len: int, vocab_size: int, model: BaseLLMModel):
        """TODO: implement `_capture_graphs`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _capture_graphs()")

    def can_use_cuda_graph(self, batch: Batch) -> bool:
        """TODO: implement `can_use_cuda_graph`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement can_use_cuda_graph()")

    def replay(self, batch: Batch) -> torch.Tensor:
        """TODO: implement `replay`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement replay()")

    def pad_batch(self, batch: Batch) -> None:
        """TODO: implement `pad_batch`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement pad_batch()")

    def destroy_cuda_graphs(self) -> None:
        """TODO: implement `destroy_cuda_graphs`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement destroy_cuda_graphs()")


logger: Any = None
