"""Online Qwen trace replay scaffold."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Qwen online trace benchmark scaffold")
    parser.add_argument("--base-url", default="http://127.0.0.1:1919")
    parser.add_argument("--trace", required=True)
    parser.parse_args(argv)
    raise NotImplementedError("Implement trace replay and latency percentile collection")


if __name__ == "__main__":
    raise SystemExit(main())
