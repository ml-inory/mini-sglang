"""Teaching scaffold for minisgl.models.qwen2.

Scaffold for minisgl.models.qwen2.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class Qwen2DecoderLayer:
    """TODO: implement `Qwen2DecoderLayer`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig, layer_id: int):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(
        self, x: torch.Tensor, residual: torch.Tensor | None = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class Qwen2Model:
    """TODO: implement `Qwen2Model`. (original base: BaseOP)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


class Qwen2ForCausalLM:
    """TODO: implement `Qwen2ForCausalLM`. (original base: BaseLLMModel)"""

    def __init__(self, config: ModelConfig):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def forward(self) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")


__all__ = [
    "Qwen2ForCausalLM",
]
