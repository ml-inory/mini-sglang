"""Teaching scaffold for minisgl.engine.config.

Scaffold for minisgl.engine.config.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class EngineConfig:
    """TODO: implement `EngineConfig`."""

    def hf_config(self):
        """TODO: implement `hf_config`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement hf_config()")

    def model_config(self) -> ModelConfig:
        """TODO: implement `model_config`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement model_config()")

    @property
    def max_seq_len(self) -> int:
        """TODO: implement `max_seq_len`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement max_seq_len()")

    @property
    def max_forward_len(self) -> int:
        """TODO: implement `max_forward_len`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement max_forward_len()")

    @property
    def distributed_addr(self) -> str:
        """TODO: implement `distributed_addr`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement distributed_addr()")
