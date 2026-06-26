"""CLI skeleton for running workload traces against AVL or BST implementations."""

from __future__ import annotations

import argparse
from pathlib import Path


def run_trace(tree_type: str, trace_path: Path, out_path: Path) -> None:
    """Run a trace file against the selected tree implementation."""
    # TODO: Read the trace file.
    # TODO: Dispatch operations to AVLTree or BSTree.
    # TODO: Write candidate output in the expected format.
    _ = (tree_type, trace_path, out_path)


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for trace execution."""
    parser = argparse.ArgumentParser(description="Run a trace against a tree implementation.")
    parser.add_argument("--tree", choices=("avl", "bst"), required=True, help="Tree implementation to use.")
    parser.add_argument("--trace", required=True, type=Path, help="Path to the input trace file.")
    parser.add_argument("--out", required=True, type=Path, help="Path to write the candidate output.")
    return parser


def main() -> None:
    """Parse CLI arguments and call the trace runner placeholder."""
    parser = build_parser()
    args = parser.parse_args()
    run_trace(tree_type=args.tree, trace_path=args.trace, out_path=args.out)


if __name__ == "__main__":
    main()
