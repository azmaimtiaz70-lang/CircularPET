"""
plots.py
--------
Generates figures from the Monte Carlo uncertainty analysis (uncertainty.py).

Produces two figures, saved to results/figures/:
  1. box_comparison.png   - spread of outcomes per pathway (box plot)
  2. win_percentage.png   - how often each pathway "wins" (bar chart)

Run this AFTER uncertainty.py works, since it reuses the same simulation.
"""

import os
import matplotlib.pyplot as plt
from uncertainty import run_simulation, N_SIMULATIONS

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "figures")


def plot_box_comparison(results):
    """Box plot showing the distribution of outcomes for each pathway."""
    fig, ax = plt.subplots(figsize=(8, 5))

    labels = list(results.keys())
    data = [results[name] for name in labels]

    ax.boxplot(data, tick_labels=labels, showfliers=False)
    ax.axhline(0, color="gray", linestyle="--", linewidth=1)
    ax.set_ylabel("Net GHG Impact (kg CO2-eq per ton PET waste)")
    ax.set_title(f"Distribution of Pathway Impacts Across {N_SIMULATIONS} Simulations")
    plt.setp(ax.get_xticklabels(), rotation=15, ha="right")
    plt.tight_layout()

    out_path = os.path.join(FIGURES_DIR, "box_comparison.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved: {out_path}")


def plot_win_percentage(win_counts, n_simulations):
    """Bar chart showing how often each pathway had the lowest impact."""
    fig, ax = plt.subplots(figsize=(7, 5))

    labels = list(win_counts.keys())
    percentages = [100 * win_counts[name] / n_simulations for name in labels]

    bars = ax.bar(labels, percentages, color=["#2E7D32", "#1565C0", "#EF6C00", "#616161"])
    ax.set_ylabel("Win Rate (%)")
    ax.set_title("How Often Each Pathway is the Lowest-Impact Choice")
    plt.setp(ax.get_xticklabels(), rotation=15, ha="right")
    ax.set_ylim(0, 100)

    for bar, pct in zip(bars, percentages):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                 f"{pct:.1f}%", ha="center", va="bottom")

    plt.tight_layout()

    out_path = os.path.join(FIGURES_DIR, "win_percentage.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    os.makedirs(FIGURES_DIR, exist_ok=True)

    print("Running simulation...")
    results, win_counts = run_simulation()

    plot_box_comparison(results)
    plot_win_percentage(win_counts, N_SIMULATIONS)

    print("\nDone. Check results/figures/ for the saved images.")
    

