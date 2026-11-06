"""Teaching scaffold for minisgl.utils.registry.

Scaffold for minisgl.utils.registry.

Every behavior is intentionally left for the learner. See:
- docs/code-map.md for the subsystem map
- docs/index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class Registry:
    """TODO: implement `Registry`. (original base: Generic[T])"""

    def __init__(self, type: str):
        """TODO: implement `__init__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __init__()")

    def register(self, name: str) -> Callable[[T], None]:
        """TODO: implement `register`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement register()")

    def __getitem__(self, name: str) -> T:
        """TODO: implement `__getitem__`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __getitem__()")

    def supported_names(self) -> List[str]:
        """TODO: implement `supported_names`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement supported_names()")

    def assert_supported(self, names: str | Iterable[str]) -> None:
        """TODO: implement `assert_supported`. Read docs/code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement assert_supported()")


T: Any = None
