"""Teaching scaffold for minisgl.kvcache.base.

Scaffold for minisgl.kvcache.base.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseKVCachePool:
    """Base class for key-value caches.
    This class defines the interface for key-value caches used.
    """

    def k_cache(self, index: int) -> torch.Tensor:
        """TODO: implement `k_cache`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement k_cache()")

    def v_cache(self, index: int) -> torch.Tensor:
        """TODO: implement `v_cache`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement v_cache()")

    def store_kv(
        self, k: torch.Tensor, v: torch.Tensor, out_loc: torch.Tensor, layer_id: int
    ) -> None:
        """TODO: implement `store_kv`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement store_kv()")

    @property
    def device(self) -> torch.device:
        """TODO: implement `device`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement device()")

    @property
    def dtype(self) -> torch.dtype:
        """TODO: implement `dtype`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement dtype()")

    @property
    def num_layers(self) -> int:
        """TODO: implement `num_layers`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement num_layers()")


class BaseCacheHandle:
    """TODO: implement `BaseCacheHandle`. (original base: ABC)"""

    def get_matched_indices(self) -> torch.Tensor:
        """TODO: implement `get_matched_indices`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_matched_indices()")


class SizeInfo:
    """TODO: implement `SizeInfo`. (original base: NamedTuple)"""

    @property
    def total_size(self) -> int:
        """TODO: implement `total_size`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement total_size()")


class InsertResult:
    """TODO: implement `InsertResult`. (original base: NamedTuple)"""

    """TODO: replace this marker with the InsertResult implementation."""


class MatchResult:
    """TODO: implement `MatchResult`. (original base: NamedTuple)"""

    """TODO: replace this marker with the MatchResult implementation."""


class BasePrefixCache:
    """TODO: implement `BasePrefixCache`. (original base: ABC)"""

    def lock_handle(self, handle: BaseCacheHandle, unlock: bool = False) -> None:
        """Lock or unlock a cache handle.
        This operation will not modify the cache, but change the size info only.
        When a handle is locked, it cannot be evicted.
        Handles must be locked before the previously-returned tensor of `match_prefix` is used.
        Otherwise it may be evicted by calling evict.

        Args:
            handle (BaseCacheHandle): The cache handle to lock or unlock.
            unlock (bool): Whether to unlock the handle. Defaults to False.
        """
        raise NotImplementedError("Teaching scaffold: implement lock_handle()")

    def match_prefix(self, input_ids: torch.Tensor) -> MatchResult:
        """Match prefix and return the indices of the matched prefix in the cache.
        This operation will not modify the cache.
        The returned indices is only safe to use when the handle is locked.

        Args:
            input_ids (torch.Tensor): The input ids to match. Shape: (seq_len,)
        Returns:
            MatchResult: The match result containing the cache handles.
        """
        raise NotImplementedError("Teaching scaffold: implement match_prefix()")

    def insert_prefix(self, input_ids: torch.Tensor, indices: torch.Tensor) -> InsertResult:
        """Insert a new prefix into the cache.
        This operation will modify the cache.
        Args:
            input_ids (torch.Tensor): The input ids to insert. Shape: (seq_len,)
            indices (torch.Tensor): The indices to store the new prefix. Shape: (seq_len,)

        Returns:
            InsertResult: The result of the insertion.
        """
        raise NotImplementedError("Teaching scaffold: implement insert_prefix()")

    def evict(self, size: int) -> torch.Tensor:
        """Evict some prefixes from the cache to free up space.
        This operation will modify the cache.
        Note that evict 0 is always safe and does nothing.
        Note that the actual evict size may be larger than the requested size.
        Args:
            size (int): The size to evict.

        Returns:
            torch.Tensor: The indices evicted. Shape: (evict_size,)
        Raises:
            RuntimeError: If the requested size is larger than the evictable size.
        """
        raise NotImplementedError("Teaching scaffold: implement evict()")

    def reset(self) -> None:
        """Reset the cache manager and the underlying cache."""
        raise NotImplementedError("Teaching scaffold: implement reset()")

    @property
    def size_info(self) -> SizeInfo:
        """Get the size information of the cache."""
        raise NotImplementedError("Teaching scaffold: implement size_info()")

    def check_integrity(self) -> None:
        """Check the integrity of the cache. Raise an error if the cache is corrupted."""
        raise NotImplementedError("Teaching scaffold: implement check_integrity()")
