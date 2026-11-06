"""WildChat dataset benchmark scaffold."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="WildChat benchmark scaffold")
    parser.add_argument("--dataset", required=True)
    parser.parse_args(argv)
    raise NotImplementedError("Implement dataset loading and workload replay")


if __name__ == "__main__":
    raise SystemExit(main())
