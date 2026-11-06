"""Teaching scaffold for minisgl.tokenizer.detokenize.

Scaffold for minisgl.tokenizer.detokenize.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _is_chinese_char(cp: int):
    """Checks whether CP is the codepoint of a CJK character."""
    raise NotImplementedError("Teaching scaffold: implement _is_chinese_char()")


def find_printable_text(text: str):
    """Returns the longest printable substring of text that contains only entire words."""
    raise NotImplementedError("Teaching scaffold: implement find_printable_text()")


class DecodeStatus:
    """TODO: implement `DecodeStatus`."""

    """TODO: replace this marker with the DecodeStatus implementation."""


class DetokenizeManager:
    """TODO: implement `DetokenizeManager`."""

    def __init__(self, tokenizer: PreTrainedTokenizerBase) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def detokenize(self, msgs: List[DetokenizeMsg]) -> List[str]:
        """TODO: implement `detokenize`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement detokenize()")
