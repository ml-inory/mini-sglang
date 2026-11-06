"""Teaching scaffold for minisgl.models.mistral.

Scaffold for minisgl.models.mistral.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class MistralDecoderLayer:
    """TODO: implement `MistralDecoderLayer`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig, layer_id: int):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, x: torch.Tensor, residual: torch.Tensor | None = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class MistralModel:
    """TODO: implement `MistralModel`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class MistralForCausalLM:
    """TODO: implement `MistralForCausalLM`. (original base: BaseLLMModel)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


__all__ = [
    "MistralForCausalLM",
]
