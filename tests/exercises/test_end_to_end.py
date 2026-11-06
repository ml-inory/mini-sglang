from __future__ import annotations

import os

import pytest

pytestmark = [pytest.mark.exercise, pytest.mark.integration, pytest.mark.gpu]


@pytest.mark.skipif(
    not os.getenv("MINISGL_TEST_MODEL"),
    reason="set MINISGL_TEST_MODEL to a local model path for the end-to-end chapter",
)
def test_greedy_generation_is_deterministic() -> None:
    pytest.importorskip("torch")
    from minisgl.llm import LLM

    llm = LLM(model_path=os.environ["MINISGL_TEST_MODEL"])
    first = llm.generate(["1 + 1 ="], sampling_params={"max_tokens": 8, "temperature": 0})
    second = llm.generate(["1 + 1 ="], sampling_params={"max_tokens": 8, "temperature": 0})
    assert first == second
