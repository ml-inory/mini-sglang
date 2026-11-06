"""Teaching scaffold for minisgl.env.

Scaffold for minisgl.env.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BaseEnv:
    """TODO: implement `BaseEnv`."""

    def _init(self, name: str) -> None:
        """TODO: implement `_init`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _init()")


class EnvVar:
    """TODO: implement `EnvVar`. (original base: BaseEnv, Generic[T])"""

    def __init__(self, default_value: T, fn: Callable[[str], T]):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def _init(self, name: str) -> None:
        """TODO: implement `_init`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement _init()")

    def __bool__(self):
        """TODO: implement `__bool__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __bool__()")

    def __str__(self):
        """TODO: implement `__str__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __str__()")


def _PARSE_MEM_BYTES(mem: str) -> int:
    """TODO: implement `_PARSE_MEM_BYTES`. Read docs/code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _PARSE_MEM_BYTES()")


class EnvClassSingleton:
    """TODO: implement `EnvClassSingleton`."""

    def __new__(cls):
        """TODO: implement `__new__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __new__()")

    def __init__(self) -> None:
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")


T: Any = None
_TO_BOOL: Any = None
MINISGL_ENV_PREFIX: Any = None
EnvInt: Any = None
EnvFloat: Any = None
EnvBool: Any = None
EnvOption: Any = None
EnvMem: Any = None
ENV: Any = None
