"""Offline throughput benchmark scaffold.

Suggested contract:
1. Load a fixed prompt/output-length distribution.
2. Submit all requests to ``minisgl.llm.LLM``.
3. Report request throughput, token throughput, TTFT, and inter-token latency.
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline Mini-SGLang benchmark scaffold")
    parser.add_argument("--model", required=True)
    parser.add_argument("--num-requests", type=int, default=256)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    build_parser().parse_args(argv)
    raise NotImplementedError("Implement the offline benchmark in docs/performance.md")


if __name__ == "__main__":
    raise SystemExit(main())
