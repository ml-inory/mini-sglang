"""Command-line entry point for the teaching scaffold."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser exposed by ``python -m minisgl``."""
    parser = argparse.ArgumentParser(
        prog="minisgl",
        description="Mini-SGLang teaching scaffold. Implement subsystems chapter by chapter.",
    )
    parser.add_argument("--model", help="Model path or hub id used by later serving chapters.")
    parser.add_argument(
        "--shell", action="store_true", help="Target the interactive shell chapter."
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Print the scaffold status instead of pretending to launch an engine."""
    args = build_parser().parse_args(argv)
    print("Mini-SGLang teaching scaffold: no inference backend is implemented yet.")
    print("Start with docs/index.md, then run: MINISGL_RUN_EXERCISES=1 pytest tests/exercises")
    if args.model:
        print(f"Requested model (not loaded): {args.model}")
    if args.shell:
        print("Interactive shell (not implemented).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
