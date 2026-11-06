"""Teaching scaffold for minisgl.message.tokenizer.

Scaffold for minisgl.message.tokenizer.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseTokenizerMsg:
    """TODO: implement `BaseTokenizerMsg`."""

    @staticmethod
    def encoder(msg: BaseTokenizerMsg) -> Dict:
        """TODO: implement `encoder`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement encoder()")

    @staticmethod
    def decoder(json: Dict) -> BaseTokenizerMsg:
        """TODO: implement `decoder`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement decoder()")


class BatchTokenizerMsg:
    """TODO: implement `BatchTokenizerMsg`. (original base: BaseTokenizerMsg)"""

    """TODO: replace this marker with the BatchTokenizerMsg implementation."""


class DetokenizeMsg:
    """TODO: implement `DetokenizeMsg`. (original base: BaseTokenizerMsg)"""

    """TODO: replace this marker with the DetokenizeMsg implementation."""


class TokenizeMsg:
    """TODO: implement `TokenizeMsg`. (original base: BaseTokenizerMsg)"""

    """TODO: replace this marker with the TokenizeMsg implementation."""


class AbortMsg:
    """TODO: implement `AbortMsg`. (original base: BaseTokenizerMsg)"""

    """TODO: replace this marker with the AbortMsg implementation."""
