from __future__ import annotations

import pytest

pytestmark = pytest.mark.exercise


def test_integer_alignment_helpers() -> None:
    from minisgl.utils import align_ceil, align_down, div_ceil, div_even

    assert div_ceil(9, 4) == 3
    assert align_ceil(9, 4) == 12
    assert align_down(9, 4) == 8
    assert div_even(12, 3) == 4


def test_registry_registers_and_resolves_named_factory() -> None:
    from minisgl.utils import Registry

    registry: Registry[int] = Registry("numbers")

    @registry.register("answer")
    def answer() -> int:
        return 42

    assert registry["answer"] is answer
    assert registry["answer"]() == 42
