from __future__ import annotations

import pytest

pytestmark = pytest.mark.exercise
torch = pytest.importorskip("torch")


def test_size_info_tracks_evictable_and_protected_prefixes() -> None:
    from minisgl.kvcache.base import SizeInfo

    info = SizeInfo(evictable_size=12, protected_size=4)
    assert info.total_size == 16


def test_naive_prefix_cache_matches_shared_prefix() -> None:
    from minisgl.kvcache.naive_cache import NaivePrefixCache

    cache = NaivePrefixCache(device=torch.device("cpu"))
    keys = torch.tensor([11, 12, 13, 14], dtype=torch.int32)
    values = torch.tensor([0, 4, 8, 12], dtype=torch.int32)
    cache.insert_prefix(keys, values)
    result = cache.match_prefix(torch.tensor([11, 12, 99], dtype=torch.int32))
    assert result.cuda_handle.cached_len == 2
    assert result.cuda_handle.get_matched_indices().tolist() == [0, 4]


@pytest.mark.parametrize("page_size", [1, 4])
def test_radix_cache_reuses_common_prefix(page_size: int) -> None:
    from minisgl.core import Context, set_global_ctx
    from minisgl.kvcache.radix_cache import RadixPrefixCache

    set_global_ctx(Context(page_size=page_size))
    cache = RadixPrefixCache(device=torch.device("cpu"))
    first = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8], dtype=torch.int32)
    slots = torch.arange(len(first), dtype=torch.int32)
    cache.insert_prefix(first, slots)
    result = cache.match_prefix(first[:6])
    assert result.cuda_handle.cached_len == (6 if page_size == 1 else 4)
