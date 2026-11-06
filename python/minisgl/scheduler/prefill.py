"""Teaching scaffold for minisgl.scheduler.prefill.

Scaffold for minisgl.scheduler.prefill.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class ChunkedReq:
    """TODO: implement `ChunkedReq`. (original base: Req)"""

    def append_host(self, next_token: torch.Tensor) -> None:
        """TODO: implement `append_host`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement append_host()")

    @property
    def can_decode(self) -> bool:
        """TODO: implement `can_decode`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement can_decode()")


class PrefillAdder:
    """TODO: implement `PrefillAdder`."""

    def _try_allocate_one(self, req: PendingReq) -> Tuple[BaseCacheHandle, int] | None:
        """TODO: implement `_try_allocate_one`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _try_allocate_one()")

    def _add_one_req(
        self,
        pending_req: PendingReq,
        cache_handle: BaseCacheHandle,
        table_idx: int,
        cached_len: int,
    ) -> Req:
        """TODO: implement `_add_one_req`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _add_one_req()")

    def try_add_one(self, pending_req: PendingReq) -> Req | None:
        """TODO: implement `try_add_one`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement try_add_one()")


class PrefillManager:
    """TODO: implement `PrefillManager`."""

    def add_one_req(self, req: UserMsg) -> None:
        """TODO: implement `add_one_req`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement add_one_req()")

    def schedule_next_batch(self, prefill_budget: int) -> Batch | None:
        """TODO: implement `schedule_next_batch`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement schedule_next_batch()")

    def abort_req(self, uid: int) -> Req | None:
        """TODO: implement `abort_req`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement abort_req()")

    @property
    def runnable(self) -> bool:
        """TODO: implement `runnable`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement runnable()")


logger: Any = None
