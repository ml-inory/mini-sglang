"""Teaching scaffold for minisgl.attention.utils.

Scaffold for minisgl.attention.utils.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseCaptureData:
    """TODO: implement `BaseCaptureData`."""

    @classmethod
    def create(cls, max_bs: int, max_seq_len: int, device: torch.device, **kwargs):
        """TODO: implement `create`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement create()")
