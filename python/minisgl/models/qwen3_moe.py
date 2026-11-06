"""Teaching scaffold for minisgl.models.qwen3_moe.

Scaffold for minisgl.models.qwen3_moe.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class Qwen3DecoderLayer:
    """TODO: implement `Qwen3DecoderLayer`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig, layer_id: int):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, x: torch.Tensor, residual: torch.Tensor | None = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class Qwen3Model:
    """TODO: implement `Qwen3Model`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class Qwen3MoeForCausalLM:
    """TODO: implement `Qwen3MoeForCausalLM`. (original base: BaseLLMModel)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


__all__ = [
    "Qwen3MoeForCausalLM",
]
