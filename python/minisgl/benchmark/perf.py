"""Teaching scaffold for minisgl.benchmark.perf.

Scaffold for minisgl.benchmark.perf.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def perf_cuda(
    f: Callable[[], Any],
    *,
    init_stream: bool = True,
    repetitions: int = 10,
    cuda_graph_repetitions: int | None = 10,
) -> float:
    """TODO: implement `perf_cuda`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement perf_cuda()")


def compare_memory_kernel_perf(
    *,
    baseline: Callable[[], Any],
    our_impl: Callable[[], Any],
    memory_footprint: int,
    description: str = " ",
    extra_kwargs: Dict[str, Any] | None = None,
    need_latency: bool = True,
) -> Tuple[float, float]:
    """TODO: implement `compare_memory_kernel_perf`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement compare_memory_kernel_perf()")


logger: Any = None
