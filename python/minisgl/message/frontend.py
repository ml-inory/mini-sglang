"""Teaching scaffold for minisgl.message.frontend.

Scaffold for minisgl.message.frontend.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseFrontendMsg:
    """TODO: implement `BaseFrontendMsg`."""

    @staticmethod
    def encoder(msg: BaseFrontendMsg) -> Dict:
        """TODO: implement `encoder`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement encoder()")

    @staticmethod
    def decoder(json: Dict) -> BaseFrontendMsg:
        """TODO: implement `decoder`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement decoder()")


class BatchFrontendMsg:
    """TODO: implement `BatchFrontendMsg`. (original base: BaseFrontendMsg)"""

    """TODO: replace this marker with the BatchFrontendMsg implementation."""


class UserReply:
    """TODO: implement `UserReply`. (original base: BaseFrontendMsg)"""

    """TODO: replace this marker with the UserReply implementation."""
