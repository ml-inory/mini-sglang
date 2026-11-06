"""Teaching scaffold for minisgl.tokenizer.tokenize.

Scaffold for minisgl.tokenizer.tokenize.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class TokenizeManager:
    """TODO: implement `TokenizeManager`."""

    def __init__(self, tokenizer: PreTrainedTokenizerBase) -> None:
        """TODO: implement `__init__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def tokenize(self, msgs: List[TokenizeMsg]) -> List[torch.Tensor]:
        """TODO: implement `tokenize`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement tokenize()")
