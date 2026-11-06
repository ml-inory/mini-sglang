"""Teaching scaffold for minisgl.scheduler.cache.

Scaffold for minisgl.scheduler.cache.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class CacheManager:
    """TODO: implement `CacheManager`."""

    def __init__(self, num_pages: int, page_size: int, page_table: torch.Tensor, type: str):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def match_req(self, req: PendingReq) -> MatchResult:
        """TODO: implement `match_req`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement match_req()")

    @property
    def available_size(self) -> int:
        """TODO: implement `available_size`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement available_size()")

    def lock(self, handle: BaseCacheHandle) -> None:
        """TODO: implement `lock`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement lock()")

    def unlock(self, handle: BaseCacheHandle) -> None:
        """TODO: implement `unlock`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement unlock()")

    def allocate_paged(self, reqs: List[Req]) -> None:
        """TODO: implement `allocate_paged`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement allocate_paged()")

    def cache_req(self, req: Req, *, finished: bool) -> None:
        """TODO: implement `cache_req`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement cache_req()")

    def check_integrity(self) -> None:
        """TODO: implement `check_integrity`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement check_integrity()")

    def lazy_free_region(self):
        """TODO: implement `lazy_free_region`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement lazy_free_region()")

    def _allocate(self, needed_pages: int) -> torch.Tensor:
        """TODO: implement `_allocate`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _allocate()")

    def _free(self, indices: torch.Tensor) -> None:
        """TODO: implement `_free`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _free()")

    def _page_to_token(self, pages: torch.Tensor) -> torch.Tensor:
        """TODO: implement `_page_to_token`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _page_to_token()")


def _write_page_table(
    page_table: torch.Tensor,
    allocated: torch.Tensor,
    allocation_info: List[Tuple[int, int, int]],
    page_size: int,
) -> None:
    """TODO: implement `_write_page_table`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _write_page_table()")
