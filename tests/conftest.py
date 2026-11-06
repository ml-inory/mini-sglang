"""Shared pytest configuration for the scaffold and chapter exercises."""

from __future__ import annotations

import os

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """Expose an explicit switch for red-green exercises."""
    parser.addoption(
        "--run-exercises",
        action="store_true",
        default=False,
        help="Run chapter exercises instead of skipping them.",
    )


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Keep the clean scaffold run green until the learner opts in."""
    env_enabled = os.getenv("MINISGL_RUN_EXERCISES", "").lower() in {"1", "true", "yes"}
    if config.getoption("--run-exercises") or env_enabled:
        return

    skip = pytest.mark.skip(
        reason="chapter exercise: rerun with --run-exercises or MINISGL_RUN_EXERCISES=1"
    )
    for item in items:
        if "exercise" in item.keywords:
            item.add_marker(skip)


@pytest.fixture
def require_cuda() -> None:
    """Skip when a CUDA-capable PyTorch build is unavailable."""
    torch = pytest.importorskip("torch")
    if not torch.cuda.is_available():
        pytest.skip("requires CUDA")


@pytest.fixture
def simple_token_ids() -> list[int]:
    """Stable token sequence used by CPU-only examples."""
    return [1, 2, 3, 4, 5, 6, 7, 8]
