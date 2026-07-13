"""Benchmark runner for AVL vs BST comparison."""

from __future__ import annotations

import argparse
import csv
import os
import random
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path
from time import perf_counter_ns

from src.avl_tree import AVLTree
from src.bst_tree import BSTree


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for benchmarks."""
    parser = argparse.ArgumentParser(description="Run project benchmarks.")
    parser.add_argument(
        "--sweep",
        action="store_true",
        help="Run the complete parameter sweep.",
    )
    parser.add_argument(
        "--trace",
        type=Path,
        help="Path to a single trace file to benchmark.",
    )
    parser.add_argument(
        "--tree",
        choices=("avl", "bst"),
        help="Tree implementation to use (required with --trace).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("results/benchmark_results.csv"),
        help="CSV path for benchmark results.",
    )
    parser.add_argument(
        "--max-size",
        type=int,
        default=500000,
        help="Maximum workload size for the sweep (default: 500,000).",
    )
    return parser


def load_trace(trace_path: Path) -> list[tuple[str, int]]:
    """Load trace operations into memory to minimize disk I/O during timing."""
    operations = []
    with trace_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) == 2:
                op, value = parts
                operations.append((op, int(value)))
    return operations


def run_benchmark(
    tree_type: str, operations: list[tuple[str, int]]
) -> dict[str, list[int]]:
    """Execute trace operations on the tree and record nanosecond times."""
    if tree_type == "avl":
        tree = AVLTree()
    elif tree_type == "bst":
        tree = BSTree()
    else:
        raise ValueError(f"Unknown tree: {tree_type}")

    # Warm-up to reduce initial overhead
    for _ in range(500):
        tree.insert(random.randint(-10000, 10000))
    if tree_type == "avl":
        tree = AVLTree()
    else:
        tree = BSTree()

    times: dict[str, list[int]] = {
        "I": [],
        "D": [],
        "S": [],
        "all": [],
    }

    for op, key in operations:
        start = perf_counter_ns()
        if op == "I":
            tree.insert(key)
        elif op == "D":
            tree.delete(key)
        elif op == "S":
            tree.search(key)
        else:
            continue
        end = perf_counter_ns()
        duration = end - start
        times[op].append(duration)
        times["all"].append(duration)

    return times


def compute_stats(times: list[int]) -> dict[str, float]:
    """Calculate descriptive statistics for a list of times (in ns)."""
    if not times:
        return {
            "mean": 0.0,
            "p50": 0.0,
            "p99": 0.0,
            "min": 0.0,
            "max": 0.0,
        }
    sorted_times = sorted(times)
    n = len(sorted_times)
    mean_val = sum(sorted_times) / n
    p50_val = sorted_times[n // 2]
    p99_val = sorted_times[int(n * 0.99)]
    return {
        "mean": mean_val,
        "p50": float(p50_val),
        "p99": float(p99_val),
        "min": float(sorted_times[0]),
        "max": float(sorted_times[-1]),
    }


def write_results_to_csv(
    writer: csv.DictWriter,
    tree_type: str,
    insert_order: str,
    theta: float,
    size: int,
    ops: int,
    times_dict: dict[str, list[int]],
) -> None:
    """Compute statistics and write them to the CSV output."""
    op_map = {
        "all": "all",
        "I": "insert",
        "D": "delete",
        "S": "search",
    }
    for key, label in op_map.items():
        times = times_dict[key]
        stats = compute_stats(times)
        writer.writerow({
            "tree_type": tree_type,
            "insert_order": insert_order,
            "theta": theta,
            "size": size,
            "ops": ops,
            "op_type": label,
            "count": len(times),
            "mean_ns": stats["mean"],
            "p50_ns": stats["p50"],
            "p99_ns": stats["p99"],
            "min_ns": stats["min"],
            "max_ns": stats["max"],
        })


def generate_trace_file(
    size: int,
    ops: int,
    theta: float,
    insert_order: str,
    mix: str,
    seed: int,
    temp_dir: str,
) -> Path:
    """Generate a workload trace file using the gen_workload_1.py script."""
    temp_prefix = os.path.join(temp_dir, f"temp_workload_s{size}_t{theta}_{insert_order}")
    script_path = Path(__file__).parent.parent.parent / "gm-sidnei" / "gen_workload_1.py"
    
    cmd = [
        sys.executable,
        str(script_path),
        "generate",
        "--synthetic", str(size),
        "--out", temp_prefix,
        "--ops", str(ops),
        "--theta", str(theta),
        "--insert-order", insert_order,
        "--mix", mix,
        "--seed", str(seed),
    ]
    
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return Path(f"{temp_prefix}.trace")


def main() -> None:
    """Parse CLI arguments and run the specified benchmark mode."""
    parser = build_parser()
    args = parser.parse_args()

    if not args.sweep and not args.trace:
        parser.print_help()
        sys.exit("Error: Either --sweep or --trace must be specified.")

    # Ensure results directory exists
    args.out.parent.mkdir(parents=True, exist_ok=True)

    csv_fields = [
        "tree_type",
        "insert_order",
        "theta",
        "size",
        "ops",
        "op_type",
        "count",
        "mean_ns",
        "p50_ns",
        "p99_ns",
        "min_ns",
        "max_ns",
    ]

    if args.trace:
        if not args.tree:
            sys.exit("Error: --tree (avl|bst) is required when using --trace.")
        print(f"Loading trace: {args.trace}...")
        operations = load_trace(args.trace)
        print(f"Benchmarking {args.tree} tree over {len(operations)} operations...")
        times = run_benchmark(args.tree, operations)
        
        file_exists = args.out.exists()
        with args.out.open("a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
            if not file_exists:
                writer.writeheader()
            # Extract metadata from filename if possible, otherwise use placeholders
            write_results_to_csv(
                writer=writer,
                tree_type=args.tree,
                insert_order="unknown",
                theta=-1.0,
                size=-1,
                ops=len(operations),
                times_dict=times,
            )
        print(f"Results appended to {args.out}")
        return

    # Sweep mode
    print("Starting parameter sweep...")
    file_exists = args.out.exists()
    with args.out.open("w", newline="", encoding="utf-8") as csvfile, tempfile.TemporaryDirectory() as temp_dir:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()

        # Common configuration params
        seed = 1
        mix = "60:10:30"  # Insert 60%, Delete 10%, Search 30%

        # 1. Size sweep (AVL vs BST, theta=0.6, insert_order=shuffle)
        sizes = sorted(list(set(s for s in [100, 1000, 10000, 100000, args.max_size] if s <= args.max_size)))
        
        print("\n--- Running size sweep (AVL vs BST, Theta=0.6, Shuffle) ---")
        for size in sizes:
            ops = size
            print(f"Size: {size}, Ops: {ops}...")
            trace_path = generate_trace_file(size, ops, 0.6, "shuffle", mix, seed, temp_dir)
            operations = load_trace(trace_path)

            for tree_type in ("avl", "bst"):
                print(f"  Tree: {tree_type}...")
                times = run_benchmark(tree_type, operations)
                write_results_to_csv(
                    writer=writer,
                    tree_type=tree_type,
                    insert_order="shuffle",
                    theta=0.6,
                    size=size,
                    ops=ops,
                    times_dict=times,
                )

        # 2. Insert order sweep (shuffle vs sorted)
        # For 'sorted', BST takes O(N^2) time overall, so we cap the BST sorted size at 10,000
        print("\n--- Running insert order sweep (shuffle vs sorted) ---")
        sorted_sizes_avl = sorted(list(set(s for s in [100, 1000, 10000, 100000] if s <= args.max_size)))
        
        sorted_sizes_bst = sorted(list(set(s for s in [100, 1000, 10000] if s <= args.max_size)))

        # AVL sorted
        for size in sorted_sizes_avl:
            ops = size
            print(f"AVL sorted - Size: {size}...")
            trace_path = generate_trace_file(size, ops, 0.6, "sorted", mix, seed, temp_dir)
            operations = load_trace(trace_path)
            times = run_benchmark("avl", operations)
            write_results_to_csv(
                writer=writer,
                tree_type="avl",
                insert_order="sorted",
                theta=0.6,
                size=size,
                ops=ops,
                times_dict=times,
            )

        # BST sorted
        for size in sorted_sizes_bst:
            ops = size
            print(f"BST sorted - Size: {size}...")
            trace_path = generate_trace_file(size, ops, 0.6, "sorted", mix, seed, temp_dir)
            operations = load_trace(trace_path)
            times = run_benchmark("bst", operations)
            write_results_to_csv(
                writer=writer,
                tree_type="bst",
                insert_order="sorted",
                theta=0.6,
                size=size,
                ops=ops,
                times_dict=times,
            )

        # 3. Theta sensitivity sweep (AVL only, theta in {0.0, 0.6, 0.99, 1.2})
        print("\n--- Running theta sensitivity sweep (AVL, Shuffle) ---")
        thetas = [0.0, 0.6, 0.99, 1.2]
        theta_sizes = sorted(list(set(s for s in [100, 1000, 10000, 100000, args.max_size] if s <= args.max_size)))
        
        for theta in thetas:
            # Skip theta 0.6 as it is already covered in size sweep for AVL, but to be safe and simple we can run/re-run or write
            for size in theta_sizes:
                ops = size
                print(f"Theta: {theta}, Size: {size}...")
                trace_path = generate_trace_file(size, ops, theta, "shuffle", mix, seed, temp_dir)
                operations = load_trace(trace_path)
                times = run_benchmark("avl", operations)
                write_results_to_csv(
                    writer=writer,
                    tree_type="avl",
                    insert_order="shuffle",
                    theta=theta,
                    size=size,
                    ops=ops,
                    times_dict=times,
                )

    print(f"\nAll benchmark sweep results written to {args.out}")


if __name__ == "__main__":
    main()
