"""Teaching scaffold for minisgl.message.backend.

Scaffold for minisgl.message.backend.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseBackendMsg:
    """TODO: implement `BaseBackendMsg`."""

    def encoder(self) -> Dict:
        """TODO: implement `encoder`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement encoder()")

    @staticmethod
    def decoder(json: Dict) -> BaseBackendMsg:
        """TODO: implement `decoder`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement decoder()")


class BatchBackendMsg:
    """TODO: implement `BatchBackendMsg`. (original base: BaseBackendMsg)"""

    """TODO: replace this marker with the BatchBackendMsg implementation."""


class ExitMsg:
    """TODO: implement `ExitMsg`. (original base: BaseBackendMsg)"""

    """TODO: replace this marker with the ExitMsg implementation."""


class UserMsg:
    """TODO: implement `UserMsg`. (original base: BaseBackendMsg)"""

    """TODO: replace this marker with the UserMsg implementation."""


class AbortBackendMsg:
    """TODO: implement `AbortBackendMsg`. (original base: BaseBackendMsg)"""

    """TODO: replace this marker with the AbortBackendMsg implementation."""
