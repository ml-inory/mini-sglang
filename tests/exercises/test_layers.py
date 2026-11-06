from __future__ import annotations

import pytest

pytestmark = pytest.mark.exercise
torch = pytest.importorskip("torch")
pytest.importorskip("flashinfer")


def test_silu_and_mul_matches_reference_formula() -> None:
    import torch.nn.functional as F

    from minisgl.layers.activation import silu_and_mul

    x = torch.randn(2, 8)
    gate, value = x.chunk(2, dim=-1)
    assert torch.allclose(silu_and_mul(x), F.silu(gate) * value)
