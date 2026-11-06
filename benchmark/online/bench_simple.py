"""Simple online benchmark scaffold."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Simple online benchmark scaffold")
    parser.add_argument("--base-url", default="http://127.0.0.1:1919")
    parser.add_argument("--concurrency", type=int, default=1)
    parser.parse_args(argv)
    raise NotImplementedError("Implement concurrent request generation and metrics")


if __name__ == "__main__":
    raise SystemExit(main())
