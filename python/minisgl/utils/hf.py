"""Teaching scaffold for minisgl.utils.hf.

Scaffold for minisgl.utils.hf.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class DisabledTqdm:
    """TODO: implement `DisabledTqdm`. (original base: tqdm)"""

    def __init__(self, *args, **kwargs):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")


def load_tokenizer(model_path: str) -> PreTrainedTokenizerBase:
    """TODO: implement `load_tokenizer`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement load_tokenizer()")


def _load_hf_config(model_path: str) -> Any:
    """TODO: implement `_load_hf_config`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _load_hf_config()")


def cached_load_hf_config(model_path: str) -> PretrainedConfig:
    """TODO: implement `cached_load_hf_config`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement cached_load_hf_config()")


def download_hf_weight(model_path: str) -> str:
    """TODO: implement `download_hf_weight`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement download_hf_weight()")
