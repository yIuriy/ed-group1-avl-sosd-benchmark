"""Plotting script for benchmark results using matplotlib and pandas."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser for result plotting."""
    parser = argparse.ArgumentParser(description="Plot benchmark result files.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("results/benchmark_results.csv"),
        help="Path to the benchmark CSV file.",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("results"),
        help="Directory to save the generated figures.",
    )
    return parser


def set_premium_style() -> None:
    """Set custom matplotlib style for modern, premium appearance."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Liberation Sans", "DejaVu Sans", "Arial"],
        "figure.facecolor": "#ffffff",
        "axes.facecolor": "#f9fafb",
        "axes.edgecolor": "#e5e7eb",
        "axes.grid": True,
        "grid.color": "#f3f4f6",
        "grid.linewidth": 1.0,
        "axes.labelcolor": "#1f2937",
        "xtick.color": "#4b5563",
        "ytick.color": "#4b5563",
        "text.color": "#1f2937",
        "legend.frameon": True,
        "legend.facecolor": "#ffffff",
        "legend.edgecolor": "#e5e7eb",
    })


def plot_scale_comparison(df: pd.DataFrame, outdir: Path) -> None:
    """Plot average operation time comparison (AVL vs BST) and breakdown."""
    # Filter size sweep data: theta=0.6, insert_order=shuffle
    size_df = df[(df["theta"] == 0.6) & (df["insert_order"] == "shuffle")]
    if size_df.empty:
        print("Warning: No data found for size sweep (theta=0.6, shuffle). skipping scale plot.")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        "Escala: AVL vs BST (Theta=0.6, Shuffle)\nMedição empírica de desempenho por escala",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )

    # 1. Overall comparison
    overall = size_df[size_df["op_type"] == "all"]
    avl_o = overall[overall["tree_type"] == "avl"].sort_values("size")
    bst_o = overall[overall["tree_type"] == "bst"].sort_values("size")

    ax1.plot(avl_o["size"], avl_o["mean_ns"] / 1000.0, "o-", color="#3b82f6", linewidth=2, label="AVL (Geral)")
    ax1.plot(bst_o["size"], bst_o["mean_ns"] / 1000.0, "s-", color="#ef4444", linewidth=2, label="BST Simples (Geral)")
    
    ax1.set_xscale("log")
    ax1.set_xlabel("Tamanho da Carga ($N$)", fontsize=11, fontweight="medium")
    ax1.set_ylabel("Tempo Médio por Operação (µs)", fontsize=11, fontweight="medium")
    ax1.set_title("Tempo Médio de Operações Combinadas (I:D:S = 60:10:30)", fontsize=12, pad=10)
    ax1.legend(loc="upper left")

    # 2. Breakdown
    ops = ["insert", "delete", "search"]
    colors_avl = {"insert": "#2563eb", "delete": "#1d4ed8", "search": "#1e40af"}
    colors_bst = {"insert": "#dc2626", "delete": "#b91c1c", "search": "#991b1b"}
    
    for op in ops:
        avl_op = size_df[(size_df["tree_type"] == "avl") & (size_df["op_type"] == op)].sort_values("size")
        bst_op = size_df[(size_df["tree_type"] == "bst") & (size_df["op_type"] == op)].sort_values("size")
        
        # AVL lines
        ax2.plot(
            avl_op["size"],
            avl_op["mean_ns"] / 1000.0,
            "o--",
            color=colors_avl[op],
            linewidth=1.5,
            label=f"AVL - {op.capitalize()}",
        )
        # BST lines
        ax2.plot(
            bst_op["size"],
            bst_op["mean_ns"] / 1000.0,
            "s--",
            color=colors_bst[op],
            linewidth=1.5,
            label=f"BST - {op.capitalize()}",
        )

    ax2.set_xscale("log")
    ax2.set_xlabel("Tamanho da Carga ($N$)", fontsize=11, fontweight="medium")
    ax2.set_ylabel("Tempo Médio (µs)", fontsize=11, fontweight="medium")
    ax2.set_title("Detalhamento por Tipo de Operação", fontsize=12, pad=10)
    ax2.legend(loc="upper left", ncol=2, fontsize=9)

    plt.tight_layout()
    output_path = outdir / "scale_comparison.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Scale comparison plot saved to: {output_path}")


def plot_order_comparison(df: pd.DataFrame, outdir: Path) -> None:
    """Plot performance comparison for sorted vs shuffled insertions."""
    # Filter data: theta=0.6, op_type='all'
    order_df = df[(df["theta"] == 0.6) & (df["op_type"] == "all")]
    if order_df.empty:
        print("Warning: No data found for order comparison. Skipping order plot.")
        return

    plt.figure(figsize=(9, 6))
    
    # 4 cases: AVL shuffle, AVL sorted, BST shuffle, BST sorted
    cases = [
        ("avl", "shuffle", "#3b82f6", "o-", "AVL (Shuffle)"),
        ("avl", "sorted", "#1d4ed8", "D-", "AVL (Sorted)"),
        ("bst", "shuffle", "#ef4444", "s-", "BST Simples (Shuffle)"),
        ("bst", "sorted", "#b91c1c", "x-", "BST Simples (Sorted)"),
    ]

    for tree, order, color, marker, label in cases:
        subset = order_df[(order_df["tree_type"] == tree) & (order_df["insert_order"] == order)].sort_values("size")
        if not subset.empty:
            plt.plot(
                subset["size"],
                subset["mean_ns"] / 1000.0,
                marker,
                color=color,
                linewidth=2,
                label=label,
            )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamanho da Carga ($N$)", fontsize=11, fontweight="medium")
    plt.ylabel("Tempo Médio por Operação (µs, escala log)", fontsize=11, fontweight="medium")
    plt.title(
        "Caso Patológico: Entrada Shuffle vs Sorted (Theta=0.6)\nComparação do efeito de balanceamento no pior caso",
        fontsize=12,
        fontweight="bold",
        pad=15,
    )
    plt.legend(loc="upper left")
    plt.grid(True, which="both", linestyle="-", alpha=0.2)

    plt.tight_layout()
    output_path = outdir / "order_comparison.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Order comparison plot saved to: {output_path}")


def plot_theta_sensitivity(df: pd.DataFrame, outdir: Path) -> None:
    """Plot AVL tree sensitivity to theta values (Zipfian bias)."""
    # Filter data: tree_type='avl', insert_order='shuffle'
    theta_df = df[(df["tree_type"] == "avl") & (df["insert_order"] == "shuffle")]
    if theta_df.empty:
        print("Warning: No data found for theta sensitivity. Skipping theta plot.")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        "Sensibilidade ao Enviesamento (Zipfian Theta) - Árvore AVL\nImpacto do viés de acessos na localidade de cache e rotações",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )

    thetas = [0.0, 0.6, 0.99, 1.2]
    colors = {0.0: "#6b7280", 0.6: "#3b82f6", 0.99: "#8b5cf6", 1.2: "#ec4899"}
    markers = {0.0: "o-", 0.6: "s-", 0.99: "D-", 1.2: "^-"}

    # Left panel: Overall average
    for theta in thetas:
        subset = theta_df[(theta_df["theta"] == theta) & (theta_df["op_type"] == "all")].sort_values("size")
        if not subset.empty:
            ax1.plot(
                subset["size"],
                subset["mean_ns"] / 1000.0,
                markers[theta],
                color=colors[theta],
                linewidth=2,
                label=f"Theta = {theta}",
            )
    ax1.set_xscale("log")
    ax1.set_xlabel("Tamanho da Carga ($N$)", fontsize=11, fontweight="medium")
    ax1.set_ylabel("Tempo Médio por Operação (µs)", fontsize=11, fontweight="medium")
    ax1.set_title("Tempo Médio de Todas as Operações", fontsize=12, pad=10)
    ax1.legend(loc="upper left")

    # Right panel: Search operation
    for theta in thetas:
        subset = theta_df[(theta_df["theta"] == theta) & (theta_df["op_type"] == "search")].sort_values("size")
        if not subset.empty:
            ax2.plot(
                subset["size"],
                subset["mean_ns"] / 1000.0,
                markers[theta],
                color=colors[theta],
                linewidth=2,
                label=f"Theta = {theta}",
            )
    ax2.set_xscale("log")
    ax2.set_xlabel("Tamanho da Carga ($N$)", fontsize=11, fontweight="medium")
    ax2.set_ylabel("Tempo Médio de Busca (µs)", fontsize=11, fontweight="medium")
    ax2.set_title("Tempo Médio de Busca (Operação S)", fontsize=12, pad=10)
    ax2.legend(loc="upper left")

    plt.tight_layout()
    output_path = outdir / "theta_sensitivity.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Theta sensitivity plot saved to: {output_path}")


def main() -> None:
    """Parse CLI arguments and generate the plotting suite."""
    parser = build_parser()
    args = parser.parse_args()

    if not args.input.exists():
        sys.exit(f"Error: Input file {args.input} does not exist.")

    args.outdir.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading results from {args.input}...")
    df = pd.read_csv(args.input)

    set_premium_style()

    print("Generating plots...")
    plot_scale_comparison(df, args.outdir)
    plot_order_comparison(df, args.outdir)
    plot_theta_sensitivity(df, args.outdir)
    print("Done plotting results!")


if __name__ == "__main__":
    main()
