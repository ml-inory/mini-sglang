"""Teaching scaffold for minisgl.models.llama.

Scaffold for minisgl.models.llama.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class LlamaDecoderLayer:
    """TODO: implement `LlamaDecoderLayer`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig, layer_id: int):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, x: torch.Tensor, residual: torch.Tensor | None = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class LlamaModel:
    """TODO: implement `LlamaModel`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class LlamaForCausalLM:
    """TODO: implement `LlamaForCausalLM`. (original base: BaseLLMModel)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


__all__ = [
    "LlamaForCausalLM",
]
