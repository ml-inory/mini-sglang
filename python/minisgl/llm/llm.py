"""Teaching scaffold for minisgl.llm.llm.

Scaffold for minisgl.llm.llm.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class RequestAllFinished:
    """TODO: implement `RequestAllFinished`. (original base: Exception)"""

    """TODO: replace this marker with the RequestAllFinished implementation."""


class RequestStatus:
    """TODO: implement `RequestStatus`."""

    """TODO: replace this marker with the RequestStatus implementation."""


class LLM:
    """TODO: implement `LLM`. (original base: Scheduler)"""

    def __init__(self, model_path: str, dtype: torch.dtype = ..., **kwargs):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def _tokenize_one(self, prompt: List[int] | str) -> torch.Tensor:
        """TODO: implement `_tokenize_one`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _tokenize_one()")

    def offline_receive_msg(self, blocking: bool = False) -> List[BaseBackendMsg]:
        """TODO: implement `offline_receive_msg`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement offline_receive_msg()")

    def offline_send_result(self, reply: List[DetokenizeMsg]) -> None:
        """TODO: implement `offline_send_result`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement offline_send_result()")

    def generate(
        self,
        prompts: List[str] | List[List[int]],
        sampling_params: List[SamplingParams] | SamplingParams,
    ) -> List[Dict[str, str | List[int]]]:
        """TODO: implement `generate`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement generate()")
