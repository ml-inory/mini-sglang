"""Teaching scaffold for minisgl.tokenizer.server.

Scaffold for minisgl.tokenizer.server.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def _unwrap_msg(msg: BaseTokenizerMsg) -> List[BaseTokenizerMsg]:
    """TODO: implement `_unwrap_msg`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _unwrap_msg()")


def tokenize_worker(
    *,
    tokenizer_path: str,
    addr: str,
    create: bool,
    backend_addr: str,
    frontend_addr: str,
    local_bs: int,
    tokenizer_id: int = -1,
    model_source: str = "huggingface",
    ack_queue: mp.Queue[str] | None = None,
) -> None:
    """TODO: implement `tokenize_worker`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement tokenize_worker()")
