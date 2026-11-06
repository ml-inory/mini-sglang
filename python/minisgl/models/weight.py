"""Teaching scaffold for minisgl.models.weight.

Scaffold for minisgl.models.weight.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _shard_tensor(key: str, value: torch.Tensor, r: int, n: int, num_kv_heads: int):
    """Extract rank r's shard from a single tensor. Returns a contiguous copy."""
    raise NotImplementedError("Teaching scaffold: implement _shard_tensor()")


def _get_merge_info(key: str):
    """If key belongs to a merge group, return (merged_key, slot, all_slots). Else None."""
    raise NotImplementedError("Teaching scaffold: implement _get_merge_info()")


def _get_expert_stack_info(key: str) -> tuple[str, int] | None:
    """Map an expert-scoped checkpoint key to the packed runtime key."""
    raise NotImplementedError("Teaching scaffold: implement _get_expert_stack_info()")


def load_weight(model_path: str, device: torch.device) -> Iterator[Tuple[str, torch.Tensor]]:
    """Streaming weight loader. Yields (name, tensor) pairs already sharded, merged,
    and on device. Peak CPU memory: one full tensor + a small merge buffer.
    """
    raise NotImplementedError("Teaching scaffold: implement load_weight()")


_SPLIT_DIM_0: Any = None
_SPLIT_DIM_1: Any = None
_MERGE_GROUPS: Any = None
_SLOT_NAMES: Any = None
_EXPERT_PATTERN: Any = None
