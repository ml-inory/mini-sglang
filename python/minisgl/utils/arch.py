"""Teaching scaffold for minisgl.utils.arch.

Scaffold for minisgl.utils.arch.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _get_torch_cuda_version() -> Tuple[int, int] | None:
    """TODO: implement `_get_torch_cuda_version`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _get_torch_cuda_version()")


def is_arch_supported(major: int, minor: int = 0) -> bool:
    """TODO: implement `is_arch_supported`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement is_arch_supported()")


def is_sm90_supported() -> bool:
    """TODO: implement `is_sm90_supported`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement is_sm90_supported()")


def is_sm100_supported() -> bool:
    """TODO: implement `is_sm100_supported`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement is_sm100_supported()")
