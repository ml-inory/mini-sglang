"""Teaching scaffold for minisgl.attention.

Scaffold for minisgl.attention.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any

from minisgl.utils import Registry, init_logger

from .base import BaseAttnBackend, BaseAttnMetadata, HybridBackend


class BackendCreator:
    """TODO: implement `BackendCreator`. (original base: Protocol)"""

    def __call__(self, config: ModelConfig) -> BaseAttnBackend:
        """TODO: implement `__call__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __call__()")


def create_trtllm_backend(config: ModelConfig):
    """TODO: implement `create_trtllm_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_trtllm_backend()")


def create_fi_backend(config: ModelConfig):
    """TODO: implement `create_fi_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_fi_backend()")


def create_fa_backend(config: ModelConfig):
    """TODO: implement `create_fa_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_fa_backend()")


def validate_attn_backend(backend: str, allow_auto: bool = True):
    """TODO: implement `validate_attn_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement validate_attn_backend()")


def create_attention_backend(backend: str, config: ModelConfig) -> BaseAttnBackend:
    """TODO: implement `create_attention_backend`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement create_attention_backend()")


logger: Any = None
SUPPORTED_ATTENTION_BACKENDS: Any = None

__all__ = [
    "BaseAttnMetadata",
    "BaseAttnBackend",
    "create_attention_backend",
    "SUPPORTED_ATTENTION_BACKENDS",
    "validate_attn_backend",
]
