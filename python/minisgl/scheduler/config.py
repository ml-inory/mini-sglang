"""Teaching scaffold for minisgl.scheduler.config.

Scaffold for minisgl.scheduler.config.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _get_pid_suffix() -> str:
    """TODO: implement `_get_pid_suffix`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _get_pid_suffix()")


class SchedulerConfig:
    """TODO: implement `SchedulerConfig`. (original base: EngineConfig)"""

    @property
    def zmq_backend_addr(self) -> str:
        """TODO: implement `zmq_backend_addr`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement zmq_backend_addr()")

    @property
    def zmq_detokenizer_addr(self) -> str:
        """TODO: implement `zmq_detokenizer_addr`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement zmq_detokenizer_addr()")

    @property
    def zmq_scheduler_broadcast_addr(self) -> str:
        """TODO: implement `zmq_scheduler_broadcast_addr`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement zmq_scheduler_broadcast_addr()")

    @property
    def max_forward_len(self) -> int:
        """TODO: implement `max_forward_len`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement max_forward_len()")

    @property
    def backend_create_detokenizer_link(self) -> bool:
        """TODO: implement `backend_create_detokenizer_link`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement backend_create_detokenizer_link()")
