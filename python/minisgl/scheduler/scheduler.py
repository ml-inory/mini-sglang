"""Teaching scaffold for minisgl.scheduler.scheduler.

Scaffold for minisgl.scheduler.scheduler.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class ForwardInput:
    """TODO: implement `ForwardInput`. (original base: NamedTuple)"""

    """TODO: replace this marker with the ForwardInput implementation."""


class Scheduler:
    """TODO: implement `Scheduler`. (original base: SchedulerIOMixin)"""

    def __init__(self, config: SchedulerConfig):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def run_when_idle(self) -> None:
        """Called when the scheduler is idle to perform background tasks."""
        raise NotImplementedError("Teaching scaffold: implement run_when_idle()")

    def overlap_loop(self, last_data: ForwardData | None) -> ForwardData | None:
        """The main loop of overlapping scheduling and execution.

        It will overlap the execution of current batch and processing of last batch's results,
        which can effectively hide CPU latency and improve GPU utilization.
        """
        raise NotImplementedError("Teaching scaffold: implement overlap_loop()")

    def normal_loop(self) -> None:
        """TODO: implement `normal_loop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement normal_loop()")

    def run_forever(self) -> NoReturn:
        """TODO: implement `run_forever`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement run_forever()")

    def shutdown(self) -> None:
        """TODO: implement `shutdown`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement shutdown()")

    def _process_last_data(self, last_data: ForwardData | None) -> None:
        """TODO: implement `_process_last_data`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _process_last_data()")

    def _process_one_msg(self, msg: BaseBackendMsg) -> None:
        """TODO: implement `_process_one_msg`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _process_one_msg()")

    def _free_req_resources(self, req: Req) -> None:
        """TODO: implement `_free_req_resources`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _free_req_resources()")

    def _prepare_batch(self, batch: Batch) -> ForwardInput:
        """TODO: implement `_prepare_batch`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _prepare_batch()")

    def _schedule_next_batch(self) -> ForwardInput | None:
        """TODO: implement `_schedule_next_batch`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _schedule_next_batch()")

    def _forward(self, forward_input: ForwardInput) -> ForwardOutput:
        """TODO: implement `_forward`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _forward()")


def _make_positions(batch: Batch, device: torch.device) -> torch.Tensor:
    """TODO: implement `_make_positions`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _make_positions()")


def _make_input_tuple(batch: Batch, device: torch.device) -> Indice2D:
    """TODO: implement `_make_input_tuple`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _make_input_tuple()")


def _make_write_tuple(batch: Batch, device: torch.device) -> Indice2D:
    """TODO: implement `_make_write_tuple`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _make_write_tuple()")


logger: Any = None
Indice2D: Any = None
ForwardData: Any = None
