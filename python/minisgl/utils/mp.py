"""Teaching scaffold for minisgl.utils.mp.

Scaffold for minisgl.utils.mp.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class ZmqPushQueue:
    """TODO: implement `ZmqPushQueue`. (original base: Generic[T])"""

    def __init__(self, addr: str, create: bool, encoder: Callable[[T], Dict]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def put(self, obj: T):
        """TODO: implement `put`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement put()")

    def stop(self):
        """TODO: implement `stop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stop()")


class ZmqAsyncPushQueue:
    """TODO: implement `ZmqAsyncPushQueue`. (original base: Generic[T])"""

    def __init__(self, addr: str, create: bool, encoder: Callable[[T], Dict]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    async def put(self, obj: T):
        """TODO: implement `put`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement put()")

    def stop(self):
        """TODO: implement `stop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stop()")


class ZmqPullQueue:
    """TODO: implement `ZmqPullQueue`. (original base: Generic[T])"""

    def __init__(self, addr: str, create: bool, decoder: Callable[[Dict], T]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def get(self) -> T:
        """TODO: implement `get`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get()")

    def get_raw(self) -> bytes:
        """TODO: implement `get_raw`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get_raw()")

    def decode(self, raw: bytes) -> T:
        """TODO: implement `decode`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement decode()")

    def empty(self) -> bool:
        """TODO: implement `empty`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement empty()")

    def stop(self):
        """TODO: implement `stop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stop()")


class ZmqAsyncPullQueue:
    """TODO: implement `ZmqAsyncPullQueue`. (original base: Generic[T])"""

    def __init__(self, addr: str, create: bool, decoder: Callable[[Dict], T]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    async def get(self) -> T:
        """TODO: implement `get`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get()")

    def stop(self):
        """TODO: implement `stop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stop()")


class ZmqPubQueue:
    """TODO: implement `ZmqPubQueue`. (original base: Generic[T])"""

    def __init__(self, addr: str, create: bool, encoder: Callable[[T], Dict]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def put_raw(self, raw: bytes):
        """TODO: implement `put_raw`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement put_raw()")

    def put(self, obj: T):
        """TODO: implement `put`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement put()")

    def stop(self):
        """TODO: implement `stop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stop()")


class ZmqSubQueue:
    """TODO: implement `ZmqSubQueue`. (original base: Generic[T])"""

    def __init__(self, addr: str, create: bool, decoder: Callable[[Dict], T]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def get(self) -> T:
        """TODO: implement `get`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement get()")

    def empty(self) -> bool:
        """TODO: implement `empty`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement empty()")

    def stop(self):
        """TODO: implement `stop`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement stop()")


T: Any = None
