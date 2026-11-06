"""Teaching scaffold for minisgl.kvcache.naive_cache.

Scaffold for minisgl.kvcache.naive_cache.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class NaiveCacheHandle:
    """TODO: implement `NaiveCacheHandle`. (original base: BaseCacheHandle)"""

    def __init__(self):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def get_matched_indices(self) -> torch.Tensor:
        """TODO: implement `get_matched_indices`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_matched_indices()")


class NaivePrefixCache:
    """TODO: implement `NaivePrefixCache`. (original base: BasePrefixCache)"""

    def __init__(self, device: torch.device):
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def lock_handle(self, handle: BaseCacheHandle, unlock: bool = False) -> None:
        """TODO: implement `lock_handle`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement lock_handle()")

    def match_prefix(self, input_ids: torch.Tensor) -> MatchResult:
        """TODO: implement `match_prefix`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement match_prefix()")

    def insert_prefix(self, input_ids: torch.Tensor, indices: torch.Tensor) -> InsertResult:
        """TODO: implement `insert_prefix`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement insert_prefix()")

    def evict(self, size: int) -> torch.Tensor:
        """TODO: implement `evict`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement evict()")

    def reset(self) -> None:
        """TODO: implement `reset`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement reset()")

    @property
    def size_info(self) -> SizeInfo:
        """TODO: implement `size_info`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement size_info()")

    def check_integrity(self) -> None:
        """TODO: implement `check_integrity`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement check_integrity()")
