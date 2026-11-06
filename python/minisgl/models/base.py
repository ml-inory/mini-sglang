"""Teaching scaffold for minisgl.models.base.

Scaffold for minisgl.models.base.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseLLMModel:
    """TODO: implement `BaseLLMModel`. (original base: ABC, BaseOP)"""

    def forward(self) -> torch.Tensor:
        """TODO: implement `forward`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward()")
