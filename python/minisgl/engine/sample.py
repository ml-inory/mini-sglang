"""Teaching scaffold for minisgl.engine.sample.

Scaffold for minisgl.engine.sample.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BatchSamplingArgs:
    """TODO: implement `BatchSamplingArgs`."""

    """TODO: replace this marker with the BatchSamplingArgs implementation."""


def make_device_tensor(data: List, dtype: torch.dtype, device: torch.device) -> torch.Tensor:
    """TODO: implement `make_device_tensor`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement make_device_tensor()")


def sample_impl(
    logits: torch.Tensor,
    temperatures: torch.Tensor,
    top_k: torch.Tensor | int | None,
    top_p: torch.Tensor | float | None,
) -> torch.Tensor:
    """TODO: implement `sample_impl`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement sample_impl()")


class Sampler:
    """TODO: implement `Sampler`."""

    def prepare(self, batch: Batch) -> BatchSamplingArgs:
        """TODO: implement `prepare`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement prepare()")

    def sample(self, logits: torch.Tensor, args: BatchSamplingArgs) -> torch.Tensor:
        """TODO: implement `sample`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement sample()")
