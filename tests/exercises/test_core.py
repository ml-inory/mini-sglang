from __future__ import annotations

import pytest

pytestmark = pytest.mark.exercise
torch = pytest.importorskip("torch")


def test_sampling_params_identify_greedy_decoding() -> None:
    from minisgl.core import SamplingParams

    assert SamplingParams(temperature=0.0).is_greedy
    assert SamplingParams(temperature=1.0, top_k=1, top_p=1.0).is_greedy
    assert not SamplingParams(temperature=0.8, top_p=1.0).is_greedy


def test_request_length_and_decode_lifecycle() -> None:
    from minisgl.core import Req, SamplingParams

    request = Req(
        input_ids=torch.tensor([1, 2, 3], dtype=torch.int32),
        table_idx=0,
        cached_len=0,
        output_len=2,
        uid=7,
        sampling_params=SamplingParams(max_tokens=2),
        cache_handle=object(),
    )
    assert request.extend_len == 3
    assert request.remain_len == 2
    request.complete_one()
    assert request.cached_len == 3
    assert request.device_len == 4
    assert request.remain_len == 1
