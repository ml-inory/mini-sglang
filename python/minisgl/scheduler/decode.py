"""Teaching scaffold for minisgl.scheduler.decode.

Scaffold for minisgl.scheduler.decode.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class DecodeManager:
    """TODO: implement `DecodeManager`."""

    def filter_reqs(self, reqs: Iterable[Req]) -> None:
        """TODO: implement `filter_reqs`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement filter_reqs()")

    def remove_req(self, req: Req) -> None:
        """TODO: implement `remove_req`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement remove_req()")

    def abort_req(self, uid: int) -> Req | None:
        """TODO: implement `abort_req`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement abort_req()")

    @property
    def inflight_tokens(self) -> int:
        """TODO: implement `inflight_tokens`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement inflight_tokens()")

    def schedule_next_batch(self) -> Batch | None:
        """TODO: implement `schedule_next_batch`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement schedule_next_batch()")

    @property
    def runnable(self) -> bool:
        """TODO: implement `runnable`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement runnable()")
