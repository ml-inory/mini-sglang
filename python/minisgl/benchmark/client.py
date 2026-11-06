"""Teaching scaffold for minisgl.benchmark.client.

Scaffold for minisgl.benchmark.client.

Every behavior is intentionally left for the learner. See:
- docs/03-code-map.md for the subsystem map
- docs/00-index.md for the recommended order
"""

from __future__ import annotations

from typing import Any


class BenchmarkTrace:
    """TODO: implement `BenchmarkTrace`."""

    """TODO: replace this marker with the BenchmarkTrace implementation."""


class BenchOneResult:
    """TODO: implement `BenchOneResult`."""

    def as_json(self) -> List[float]:
        """TODO: implement `as_json`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement as_json()")

    @staticmethod
    def from_json(raw: List[float]) -> BenchOneResult:
        """TODO: implement `from_json`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement from_json()")


class RawResult:
    """TODO: implement `RawResult`."""

    """TODO: replace this marker with the RawResult implementation."""


class Counter:
    """TODO: implement `Counter`."""

    def inc(self, n=1):
        """TODO: implement `inc`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement inc()")

    def dec(self, n=1):
        """TODO: implement `dec`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement dec()")


class Console:
    """TODO: implement `Console`."""

    def update_input(self, n=1):
        """TODO: implement `update_input`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement update_input()")

    def update_output(self, n=1):
        """TODO: implement `update_output`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement update_output()")

    def update_prefill(self, n=1):
        """TODO: implement `update_prefill`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement update_prefill()")

    def update_decode(self, n=1):
        """TODO: implement `update_decode`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement update_decode()")

    def inflight(self, n=1):
        """TODO: implement `inflight`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement inflight()")

    def log_stats(self):
        """TODO: implement `log_stats`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement log_stats()")


class BenchmarkResult:
    """TODO: implement `BenchmarkResult`."""

    def as_json(self) -> List[List[float]]:
        """TODO: implement `as_json`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement as_json()")

    @staticmethod
    def from_json(raw: List[List[float]]) -> BenchmarkResult:
        """TODO: implement `from_json`. Read docs/03-code-map.md before coding."""
        raise NotImplementedError("Teaching scaffold: implement from_json()")


def make_console(num_requests: int, sum_output_length: int, use_pbar: bool = True) -> Console:
    """TODO: implement `make_console`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement make_console()")


def generate_prompt(tokenizer: Any, n: int) -> str:
    """Generate a prompt of approximately `n` tokens using the provided tokenizer."""
    raise NotImplementedError("Teaching scaffold: implement generate_prompt()")


async def benchmark_one(
    client: OpenAI,
    prompt: str,
    output_length: int,
    model: str,
    *,
    pbar: Console | bool = True,
    extra_body: Dict[str, Any] | None = None,
    input_length: int | None = None,
) -> RawResult:
    """TODO: implement `benchmark_one`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement benchmark_one()")


async def benchmark_one_batch(
    client: OpenAI,
    prompts: List[str],
    output_lengths: List[int] | int,
    model: str,
    *,
    extra_body: Dict[str, Any] | None = None,
    input_lengths: List[int | None] | None = None,
    pbar: Console | bool = True,
) -> List[RawResult]:
    """TODO: implement `benchmark_one_batch`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement benchmark_one_batch()")


async def benchmark_trace(
    client: OpenAI, msgs: List[BenchmarkTrace], model: str, *, pbar: Console | bool = True
) -> List[RawResult]:
    """TODO: implement `benchmark_trace`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement benchmark_trace()")


def process_benchmark_results(
    raw_data: List[RawResult], tokenizer: Any = ...
) -> BenchmarkResult | None:
    """TODO: implement `process_benchmark_results`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement process_benchmark_results()")


def read_qwen_trace(
    file_path: str, tokenizer: Any, n: int | None = None, dummy: bool = False
) -> List[BenchmarkTrace]:
    """TODO: implement `read_qwen_trace`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement read_qwen_trace()")


def read_mooncake_trace(
    file_path: str, tokenizer: Any, n: int | None = None, dummy: bool = False
) -> List[BenchmarkTrace]:
    """TODO: implement `read_mooncake_trace`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement read_mooncake_trace()")


def scale_traces(traces: List[BenchmarkTrace], scale: float) -> List[BenchmarkTrace]:
    """TODO: implement `scale_traces`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement scale_traces()")


async def get_model_name(client: OpenAI) -> str:
    """TODO: implement `get_model_name`. Read docs/03-code-map.md before coding."""
    raise NotImplementedError("Teaching scaffold: implement get_model_name()")


logger: Any = None
