"""Teaching scaffold for minisgl.message.

Scaffold for minisgl.message.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from .backend import AbortBackendMsg, BaseBackendMsg, BatchBackendMsg, ExitMsg, UserMsg
from .frontend import BaseFrontendMsg, BatchFrontendMsg, UserReply
from .tokenizer import AbortMsg, BaseTokenizerMsg, BatchTokenizerMsg, DetokenizeMsg, TokenizeMsg

__all__ = [
    "AbortMsg",
    "AbortBackendMsg",
    "BaseBackendMsg",
    "BatchBackendMsg",
    "ExitMsg",
    "UserMsg",
    "BaseTokenizerMsg",
    "BatchTokenizerMsg",
    "DetokenizeMsg",
    "TokenizeMsg",
    "BaseFrontendMsg",
    "BatchFrontendMsg",
    "UserReply",
]
