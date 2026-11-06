"""Teaching scaffold for minisgl.kvcache.radix_cache.

Scaffold for minisgl.kvcache.radix_cache.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class RadixTreeNode:
    """TODO: implement `RadixTreeNode`."""

    def __init__(self, key_fn: KEY_FN, tic: int | None = None) -> None:
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def set_key_value(self, key: torch.Tensor, value: torch.Tensor) -> None:
        """TODO: implement `set_key_value`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement set_key_value()")

    def set_parent(self, parent: RadixTreeNode) -> None:
        """TODO: implement `set_parent`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement set_parent()")

    @property
    def length(self) -> int:
        """TODO: implement `length`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement length()")

    @property
    def parent(self) -> RadixTreeNode:
        """TODO: implement `parent`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement parent()")

    @property
    def value(self) -> torch.Tensor:
        """TODO: implement `value`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement value()")

    def is_root(self) -> bool:
        """TODO: implement `is_root`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_root()")

    def is_leaf(self) -> bool:
        """TODO: implement `is_leaf`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_leaf()")

    def get_match_len(self, input_ids: torch.Tensor) -> int:
        """TODO: implement `get_match_len`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_match_len()")

    def split_at(self, pos: int) -> RadixTreeNode:
        """TODO: implement `split_at`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement split_at()")

    def __lt__(self, other: RadixTreeNode) -> bool:
        """TODO: implement `__lt__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __lt__()")


class RadixCacheHandle:
    """TODO: implement `RadixCacheHandle`. (original base: BaseCacheHandle)"""

    def get_matched_indices(self) -> torch.Tensor:
        """TODO: implement `get_matched_indices`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_matched_indices()")


class RadixPrefixCache:
    """TODO: implement `RadixPrefixCache`. (original base: BasePrefixCache)"""

    def __init__(self, device: torch.device):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def lock_handle(self, handle: BaseCacheHandle, unlock: bool = False) -> None:
        """TODO: implement `lock_handle`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement lock_handle()")

    def match_prefix(self, input_ids: torch.Tensor) -> MatchResult:
        """TODO: implement `match_prefix`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement match_prefix()")

    def insert_prefix(self, input_ids: torch.Tensor, indices: torch.Tensor) -> InsertResult:
        """TODO: implement `insert_prefix`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement insert_prefix()")

    def evict(self, size: int) -> torch.Tensor:
        """TODO: implement `evict`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement evict()")

    def reset(self) -> None:
        """TODO: implement `reset`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement reset()")

    @property
    def size_info(self) -> SizeInfo:
        """TODO: implement `size_info`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement size_info()")

    def check_integrity(self) -> None:
        """TODO: implement `check_integrity`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement check_integrity()")

    def _collect_leave_nodes_for_evict(self) -> List[RadixTreeNode]:
        """TODO: implement `_collect_leave_nodes_for_evict`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _collect_leave_nodes_for_evict()")

    def _tree_walk(self, input_ids: torch.Tensor) -> Tuple[RadixTreeNode, int]:
        """TODO: implement `_tree_walk`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _tree_walk()")


def _get_key_fn(page_size: int) -> KEY_FN:
    """TODO: implement `_get_key_fn`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _get_key_fn()")


KEY_FN: Any = None
