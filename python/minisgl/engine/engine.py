"""Teaching scaffold for minisgl.engine.engine.

Scaffold for minisgl.engine.engine.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class ForwardOutput:
    """TODO: implement `ForwardOutput`. (original base: NamedTuple)"""

    """TODO: replace this marker with the ForwardOutput implementation."""


class Engine:
    """TODO: implement `Engine`."""

    def __init__(self, config: EngineConfig):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def _init_communication(self, config: EngineConfig) -> torch.distributed.ProcessGroup:
        """TODO: implement `_init_communication`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _init_communication()")

    def _load_weight_state_dict(self, config: EngineConfig) -> Dict[str, torch.Tensor]:
        """TODO: implement `_load_weight_state_dict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _load_weight_state_dict()")

    def _determine_num_pages(self, old_free_memory: int, config: EngineConfig) -> int:
        """TODO: implement `_determine_num_pages`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _determine_num_pages()")

    def _sync_get_memory(self) -> Tuple[int, int]:
        """Get the min and max free memory across TP ranks."""
        raise NotImplementedError("Teaching scaffold: implement _sync_get_memory()")

    def forward_batch(self, batch: Batch, args: BatchSamplingArgs) -> ForwardOutput:
        """TODO: implement `forward_batch`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward_batch()")

    def shutdown(self) -> None:
        """TODO: implement `shutdown`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement shutdown()")


def _align_up_32(num: int) -> int:
    """TODO: implement `_align_up_32`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _align_up_32()")


def _adjust_config(config: EngineConfig):
    """TODO: implement `_adjust_config`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _adjust_config()")


logger: Any = None
