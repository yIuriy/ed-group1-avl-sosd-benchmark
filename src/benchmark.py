"""CLI skeleton for future AVL/BST benchmark execution."""

from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path
from time import perf_counter_ns


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for benchmarks."""
    parser = argparse.ArgumentParser(description="Run project benchmarks.")
    parser.add_argument("--config", help="Optional benchmark configuration file.")
    parser.add_argument("--out", help="CSV path for benchmark results.")
    return parser


def main() -> None:
    """Parse arguments and leave hooks for future benchmark logic."""
    parser = build_parser()
    args = parser.parse_args()

    # TODO: Load benchmark inputs and workload configuration.
    # TODO: Measure execution with perf_counter_ns.
    # TODO: Aggregate runs with statistics.
    # TODO: Save benchmark results to CSV.
    _ = (args, csv, statistics, Path, perf_counter_ns)


if __name__ == "__main__":
    main()
