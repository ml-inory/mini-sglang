"""Teaching scaffold for minisgl.kvcache.

Scaffold for minisgl.kvcache.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from minisgl.utils import Registry

from .base import BaseCacheHandle, BaseKVCachePool, BasePrefixCache, MatchResult, SizeInfo


class CacheManagerCreator:
    """TODO: implement `CacheManagerCreator`. (original base: Protocol)"""

    def __call__(self, device: torch.device) -> BasePrefixCache:
        """TODO: implement `__call__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __call__()")


def create_kvcache_pool(
    model_config: ModelConfig,
    num_pages: int,
    page_size: int,
    dtype: torch.dtype,
    device: torch.device,
) -> BaseKVCachePool:
    """TODO: implement `create_kvcache_pool`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_kvcache_pool()")


def create_naive_cache(device: torch.device):
    """TODO: implement `create_naive_cache`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_naive_cache()")


def create_radix_cache(device: torch.device):
    """TODO: implement `create_radix_cache`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_radix_cache()")


def create_prefix_cache(device: torch.device, type: str) -> BasePrefixCache:
    """TODO: implement `create_prefix_cache`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_prefix_cache()")


SUPPORTED_CACHE_MANAGER: Any = None

__all__ = [
    "create_kvcache_pool",
    "create_prefix_cache",
    "BaseKVCachePool",
    "BaseCacheHandle",
    "BasePrefixCache",
    "SizeInfo",
    "MatchResult",
    "SUPPORTED_CACHE_MANAGER",
]
