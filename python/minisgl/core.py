"""Teaching scaffold for minisgl.core.

Scaffold for minisgl.core.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class SamplingParams:
    """TODO: implement `SamplingParams`."""

    @property
    def is_greedy(self) -> bool:
        """TODO: implement `is_greedy`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_greedy()")


class Req:
    """TODO: implement `Req`."""

    def __post_init__(self) -> None:
        """TODO: implement `__post_init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __post_init__()")

    @property
    def remain_len(self) -> int:
        """TODO: implement `remain_len`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement remain_len()")

    @property
    def extend_len(self) -> int:
        """TODO: implement `extend_len`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement extend_len()")

    def complete_one(self) -> None:
        """TODO: implement `complete_one`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement complete_one()")

    def append_host(self, next_token: torch.Tensor) -> None:
        """TODO: implement `append_host`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement append_host()")

    @property
    def can_decode(self) -> bool:
        """TODO: implement `can_decode`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement can_decode()")

    def __repr__(self) -> str:
        """TODO: implement `__repr__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __repr__()")


class Batch:
    """TODO: implement `Batch`."""

    @property
    def is_prefill(self) -> bool:
        """TODO: implement `is_prefill`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_prefill()")

    @property
    def is_decode(self) -> bool:
        """TODO: implement `is_decode`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement is_decode()")

    @property
    def size(self) -> int:
        """TODO: implement `size`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement size()")

    @property
    def padded_size(self) -> int:
        """TODO: implement `padded_size`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement padded_size()")


class Context:
    """TODO: implement `Context`."""

    @property
    def batch(self) -> Batch:
        """TODO: implement `batch`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement batch()")

    def forward_batch(self, batch: Batch):
        """TODO: implement `forward_batch`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement forward_batch()")


def set_global_ctx(ctx: Context):
    """TODO: implement `set_global_ctx`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement set_global_ctx()")


def get_global_ctx() -> Context:
    """TODO: implement `get_global_ctx`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_global_ctx()")


_GLOBAL_CTX: Any = None
