"""Teaching scaffold for minisgl.server.api_server.

Scaffold for minisgl.server.api_server.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


def get_global_state() -> FrontendManager:
    """TODO: implement `get_global_state`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_global_state()")


def _unwrap_msg(msg: BaseFrontendMsg) -> List[UserReply]:
    """TODO: implement `_unwrap_msg`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _unwrap_msg()")


class GenerateRequest:
    """TODO: implement `GenerateRequest`. (original base: BaseModel)"""

    """TODO: replace this marker with the GenerateRequest implementation."""


class Message:
    """TODO: implement `Message`. (original base: BaseModel)"""

    """TODO: replace this marker with the Message implementation."""


class OpenAICompletionRequest:
    """Unified request model for OpenAI-style completions and chat-completions."""

    """TODO: replace this marker with the OpenAICompletionRequest implementation."""


class ModelCard:
    """TODO: implement `ModelCard`. (original base: BaseModel)"""

    """TODO: replace this marker with the ModelCard implementation."""


class ModelList:
    """TODO: implement `ModelList`. (original base: BaseModel)"""

    """TODO: replace this marker with the ModelList implementation."""


class FrontendManager:
    """TODO: implement `FrontendManager`."""

    def new_user(self) -> int:
        """TODO: implement `new_user`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement new_user()")

    async def listen(self):
        """TODO: implement `listen`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement listen()")

    def _create_listener_once(self):
        """TODO: implement `_create_listener_once`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _create_listener_once()")

    async def send_one(self, msg: BaseTokenizerMsg):
        """TODO: implement `send_one`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement send_one()")

    async def wait_for_ack(self, uid: int):
        """TODO: implement `wait_for_ack`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement wait_for_ack()")

    async def stream_generate(self, uid: int):
        """TODO: implement `stream_generate`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stream_generate()")

    async def stream_chat_completions(self, uid: int):
        """TODO: implement `stream_chat_completions`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stream_chat_completions()")

    async def stream_with_cancellation(self, generator, request: Request, uid: int):
        """TODO: implement `stream_with_cancellation`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stream_with_cancellation()")

    async def abort_user(self, uid: int):
        """TODO: implement `abort_user`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement abort_user()")

    def shutdown(self):
        """TODO: implement `shutdown`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement shutdown()")


async def lifespan(_: FastAPI):
    """TODO: implement `lifespan`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement lifespan()")


async def generate(req: GenerateRequest, request: Request):
    """TODO: implement `generate`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement generate()")


async def v1_root():
    """TODO: implement `v1_root`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement v1_root()")


async def v1_completions(req: OpenAICompletionRequest, request: Request):
    """TODO: implement `v1_completions`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement v1_completions()")


async def available_models():
    """TODO: implement `available_models`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement available_models()")


async def shell_completion(req: OpenAICompletionRequest):
    """TODO: implement `shell_completion`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement shell_completion()")


async def shell():
    """TODO: implement `shell`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement shell()")


def run_api_server(config: ServerArgs, start_backend: Callable[[], None], run_shell: bool) -> None:
    """Run the frontend API server (FastAPI + uvicorn) and wire it to the tokenizer process via ZMQ.

    Args:
        config: Server configuration (host/port, ZMQ IPC addresses, etc).
        start_backend: Callback that launches the backend worker processes (TP schedulers +
            tokenizer/detokenizer).
        run_shell: If True, run an interactive terminal shell instead of starting uvicorn.
    """
    raise NotImplementedError("Teaching scaffold: implement run_api_server()")


logger: Any = None
_GLOBAL_STATE: Any = None
app: Any = None
