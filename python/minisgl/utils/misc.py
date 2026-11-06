"""Teaching scaffold for minisgl.utils.misc.

Scaffold for minisgl.utils.misc.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def call_if_main(name: str = "__main__", discard: bool | None = None):
    """Decorator to ensure a function will call when the script is run as main."""
    raise NotImplementedError("Teaching scaffold: implement call_if_main()")


def div_even(a: int, b: int, allow_replicate: bool = False) -> int:
    """Divides two integers. If allow_replicate=True, allows b > a when b % a == 0, returning 1."""
    raise NotImplementedError("Teaching scaffold: implement div_even()")


def div_ceil(a: int, b: int) -> int:
    """Divides two integers, rounding up"""
    raise NotImplementedError("Teaching scaffold: implement div_ceil()")


def align_ceil(a: int, b: int) -> int:
    """Aligns a to the next multiple of b"""
    raise NotImplementedError("Teaching scaffold: implement align_ceil()")


def align_down(a: int, b: int) -> int:
    """Aligns a to the previous multiple of b"""
    raise NotImplementedError("Teaching scaffold: implement align_down()")


class Unset:
    """TODO: implement `Unset`."""

    """TODO: replace this marker with the Unset implementation."""


UNSET: Any = None
