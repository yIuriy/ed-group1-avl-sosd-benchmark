"""CLI skeleton for plotting benchmark results."""

from __future__ import annotations

import argparse

import matplotlib.pyplot as plt
import pandas as pd


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for result plotting."""
    parser = argparse.ArgumentParser(description="Plot benchmark result files.")
    parser.add_argument("--input", help="Path to a benchmark CSV file.")
    parser.add_argument("--output", help="Path to save the generated figure.")
    return parser


def main() -> None:
    """Parse arguments and leave placeholders for future plotting logic."""
    parser = build_parser()
    args = parser.parse_args()

    # TODO: Load CSV results with pandas.
    # TODO: Build charts with matplotlib.
    # TODO: Save the generated figure to the requested output path.
    _ = (args, pd, plt)


if __name__ == "__main__":
    main()
