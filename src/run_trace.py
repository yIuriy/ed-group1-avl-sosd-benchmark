"""CLI skeleton for running workload traces against AVL or BST implementations."""

from __future__ import annotations

import argparse
from pathlib import Path
from .bst_tree import BSTree
from .avl_tree import AVLTree


def run_trace(tree_type: str, trace_path: Path, out_path: Path) -> None:
    """Run a trace file against the selected tree implementation."""
    if tree_type == "bst":
        tree = BSTree()
    else:
        tree = AVLTree()

    with trace_path.open("r", encoding="utf-8") as trace_file, out_path.open("w", encoding="utf-8") as out_file:
        for line in trace_file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            op, value = line.split()
            key = int(value)

            if op == "I":
                tree.insert(key)
            elif op == "D":
                tree.delete(key)
            elif op == "S":
                found = tree.search(key)
                status = "FOUND" if found else "NOT_FOUND"
                out_file.write(f"{key} {status}\n")


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
