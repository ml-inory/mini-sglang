from __future__ import annotations

import pytest

pytestmark = [pytest.mark.exercise, pytest.mark.gpu, pytest.mark.slow]
torch = pytest.importorskip("torch")


def test_kernel_indexing_matches_pytorch_embedding(require_cuda: None) -> None:
    from minisgl.kernel import indexing

    weights = torch.randn(16, 8, device="cuda", dtype=torch.float16)
    indices = torch.tensor([0, 7, 15], device="cuda", dtype=torch.int32)
    expected = torch.nn.functional.embedding(indices.long(), weights)
    assert torch.equal(indexing(weights, indices), expected)
