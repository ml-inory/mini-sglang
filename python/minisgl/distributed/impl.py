"""Teaching scaffold for minisgl.distributed.impl.

Scaffold for minisgl.distributed.impl.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class DistributedImpl:
    """TODO: implement `DistributedImpl`. (original base: ABC)"""

    def all_reduce(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_reduce`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_reduce()")

    def all_gather(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_gather`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_gather()")


class TorchDistributedImpl:
    """TODO: implement `TorchDistributedImpl`. (original base: DistributedImpl)"""

    def all_reduce(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_reduce`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_reduce()")

    def all_gather(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_gather`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_gather()")


class PyNCCLDistributedImpl:
    """TODO: implement `PyNCCLDistributedImpl`. (original base: DistributedImpl)"""

    def all_reduce(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_reduce`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_reduce()")

    def all_gather(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_gather`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_gather()")


class DistributedCommunicator:
    """TODO: implement `DistributedCommunicator`."""

    def all_reduce(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_reduce`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_reduce()")

    def all_gather(self, x: torch.Tensor) -> torch.Tensor:
        """TODO: implement `all_gather`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement all_gather()")


def enable_pynccl_distributed(
    tp_info: DistributedInfo, tp_cpu_group: torch.distributed.ProcessGroup, max_bytes: int
) -> None:
    """Enable PyNCCL-based distributed communication for tensor parallelism."""
    raise NotImplementedError("Teaching scaffold: implement enable_pynccl_distributed()")


def destroy_distributed() -> None:
    """Destroy all the distributed communication plugins."""
    raise NotImplementedError("Teaching scaffold: implement destroy_distributed()")
