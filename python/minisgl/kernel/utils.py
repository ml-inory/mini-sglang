"""Teaching scaffold for minisgl.kernel.utils.

Scaffold for minisgl.kernel.utils.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class CppArgList:
    """TODO: implement `CppArgList`. (original base: list[str])"""

    def __str__(self) -> str:
        """TODO: implement `__str__`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement __str__()")


class KernelConfig:
    """TODO: implement `KernelConfig`. (original base: NamedTuple)"""

    @property
    def template_args(self) -> str:
        """TODO: implement `template_args`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement template_args()")


def _make_name(*args: str) -> str:
    """TODO: implement `_make_name`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _make_name()")


def _make_wrapper(tup: Tuple[str, str]) -> str:
    """TODO: implement `_make_wrapper`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement _make_wrapper()")


def make_cpp_args(*args: CPP_TEMPLATE_TYPE) -> CppArgList:
    """TODO: implement `make_cpp_args`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement make_cpp_args()")


def load_aot(
    *args: str,
    cpp_files: List[str] | None = None,
    cuda_files: List[str] | None = None,
    extra_cflags: List[str] | None = None,
    extra_cuda_cflags: List[str] | None = None,
    extra_ldflags: List[str] | None = None,
    extra_include_paths: List[str] | None = None,
    build_directory: str | None = None,
) -> Module:
    """TODO: implement `load_aot`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement load_aot()")


def load_jit(
    *args: str,
    cpp_files: List[str] | None = None,
    cuda_files: List[str] | None = None,
    cpp_wrappers: List[Tuple[str, str]] | None = None,
    cuda_wrappers: List[Tuple[str, str]] | None = None,
    extra_cflags: List[str] | None = None,
    extra_cuda_cflags: List[str] | None = None,
    extra_ldflags: List[str] | None = None,
    extra_include_paths: List[str] | None = None,
    build_directory: str | None = None,
) -> Module:
    """TODO: implement `load_jit`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement load_jit()")


KERNEL_PATH: Any = None
DEFAULT_INCLUDE: Any = None
DEFAULT_CFLAGS: Any = None
DEFAULT_CUDA_CFLAGS: Any = None
DEFAULT_LDFLAGS: Any = None
CPP_TEMPLATE_TYPE: Any = None
