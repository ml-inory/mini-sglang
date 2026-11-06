"""Teaching scaffold for minisgl.layers.embedding.

Scaffold for minisgl.layers.embedding.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class VocabParallelEmbedding:
    """TODO: implement `VocabParallelEmbedding`. (original base: BaseOP)"""

    def __init__(self, num_embeddings: int, embedding_dim: int):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class ParallelLMHead:
    """TODO: implement `ParallelLMHead`. (original base: VocabParallelEmbedding)"""

    def __init__(
        self,
        num_embeddings: int,
        embedding_dim: int,
        bias: bool = False,
        tie_word_embeddings: bool = False,
        tied_embedding: VocabParallelEmbedding | None = None,
    ):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def load_state_dict(
        self, state_dict: Dict[str, torch.Tensor], *, prefix: str = "", _internal: bool = False
    ) -> None:
        """TODO: implement `load_state_dict`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement load_state_dict()")

    def state_dict(
        self, *, prefix: str = "", result: Dict[str, torch.Tensor] | None = None
    ) -> Dict[str, torch.Tensor]:
        """TODO: implement `state_dict`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement state_dict()")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
