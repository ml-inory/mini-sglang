"""Teaching scaffold for minisgl.scheduler.io.

Scaffold for minisgl.scheduler.io.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class SchedulerIOMixin:
    """Mixin class for Scheduler I/O operations.

    This class handles the communication between the scheduler and the tokenizer.

    Public Utilities:
        receive_msg: Function to receive messages from the tokenizer.
        send_result: Function to send results back to the tokenizer.
        sync_all_ranks: Function to synchronize all ranks on CPU side.
    """

    def __init__(self, config: SchedulerConfig, tp_cpu_group: torch.distributed.ProcessGroup):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def run_when_idle(self):
        """TODO: implement `run_when_idle`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement run_when_idle()")

    def offline_receive_msg(self, blocking: bool = False) -> List[BaseBackendMsg]:
        """TODO: implement `offline_receive_msg`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement offline_receive_msg()")

    def offline_send_result(self, reply: List[DetokenizeMsg]) -> None:
        """TODO: implement `offline_send_result`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement offline_send_result()")

    def sync_all_ranks(self) -> None:
        """TODO: implement `sync_all_ranks`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement sync_all_ranks()")

    def _recv_msg_single_rank(self, blocking: bool = False) -> List[BaseBackendMsg]:
        """TODO: implement `_recv_msg_single_rank`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _recv_msg_single_rank()")

    def _recv_msg_multi_rank0(self, blocking: bool = False) -> List[BaseBackendMsg]:
        """TODO: implement `_recv_msg_multi_rank0`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _recv_msg_multi_rank0()")

    def _recv_msg_multi_rank1(self, blocking: bool = False) -> List[BaseBackendMsg]:
        """TODO: implement `_recv_msg_multi_rank1`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _recv_msg_multi_rank1()")

    def _reply_tokenizer_rank0(self, reply: List[DetokenizeMsg]) -> None:
        """TODO: implement `_reply_tokenizer_rank0`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _reply_tokenizer_rank0()")

    def _reply_tokenizer_rank1(self, reply: List[DetokenizeMsg]) -> None:
        """TODO: implement `_reply_tokenizer_rank1`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _reply_tokenizer_rank1()")


logger: Any = None
