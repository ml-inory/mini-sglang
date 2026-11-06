"""Teaching scaffold for minisgl.kernel.pynccl.

Scaffold for minisgl.kernel.pynccl.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class PyNCCLCommunicator:
    """Teaching scaffold for the native PyNCCL communicator wrapper."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct a communicator around the native NCCL binding."""
        raise NotImplementedError("Teaching scaffold: implement PyNCCLCommunicator.__init__()")


def _load_nccl_module() -> Module:
    """TODO: implement `_load_nccl_module`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _load_nccl_module()")


def _get_pynccl_wrapper_cls():
    """TODO: implement `_get_pynccl_wrapper_cls`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _get_pynccl_wrapper_cls()")


def init_pynccl(
    *,
    tp_rank: int,
    tp_size: int,
    tp_cpu_group: torch.distributed.ProcessGroup,
    max_size_bytes: int = 0,
) -> PyNCCLCommunicator:
    """TODO: implement `init_pynccl`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement init_pynccl()")
