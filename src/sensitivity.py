"""
sensitivity.py
--------------
Finds which inputs matter most for the choice between mechanical and
chemical recycling.

It repeats the same simulation as uncertainty.py (same seed, same shared
inputs) but also records every input value, then measures how strongly each
input moves mechanical recycling's advantage over chemical recycling.

Advantage = (chemical impact) - (mechanical impact), in kg CO2-eq per ton.
Positive advantage means mechanical recycling is better in that run.

Outputs:
  results/tables/sensitivity.csv
  results/figures/sensitivity.png
"""

import os
import random
import matplotlib.pyplot as plt
import pandas as pd
from model import mechanical_recycling, chemical_recycling
from uncertainty import N_SIMULATIONS, RANDOM_SEED, sample_params

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")
TABLES_DIR = os.path.join(RESULTS_DIR, "tables")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")

# Inputs that are the same physical quantity for every pathway
SHARED = ["collection_rate", "virgin_emission_factor", "landfill_emission_factor"]


def run_and_record():
    random.seed(RANDOM_SEED)
    rows = []

    for _ in range(N_SIMULATIONS):
        mech = sample_params("mechanical")
        chem = sample_params("chemical")
        sample_params("energy")      # drawn only to keep the random stream
        sample_params("landfill")    # identical to uncertainty.py

        for key in SHARED:
            chem[key] = mech[key]

        row = {}
        for k, v in mech.items():
            name = k if k in SHARED else "mechanical " + k
            row[name] = v
        for k, v in chem.items():
            if k not in SHARED:
                row["chemical " + k] = v

        row["advantage"] = chemical_recycling(chem) - mechanical_recycling(mech)
        rows.append(row)

    return pd.DataFrame(rows)


def compute_sensitivity(df):
    ranks = df.rank()
    corr = ranks.corr()["advantage"].drop("advantage")
    out = corr.reset_index()
    out.columns = ["input", "rank_correlation"]
    out["size"] = out["rank_correlation"].abs()
    out = out.sort_values("size", ascending=False).drop(columns="size")
    out["input"] = (
        out["input"]
        .str.replace("_", " ")
        .str.replace("chemical chemical", "chemical")
        .str.replace("rpet", "rPET")
    )
    return out.reset_index(drop=True)


def plot_sensitivity(sens):
    top = sens.iloc[::-1]
    colors = ["#2E7D32" if v > 0 else "#C62828" for v in top["rank_correlation"]]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(top["input"], top["rank_correlation"], color=colors)
    ax.axvline(0, color="gray", linewidth=1)
    ax.set_xlabel("Rank correlation with mechanical recycling's advantage")
    ax.set_title("What decides mechanical vs chemical recycling")
    plt.tight_layout()

    out_path = os.path.join(FIGURES_DIR, "sensitivity.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    os.makedirs(TABLES_DIR, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)

    df = run_and_record()
    sens = compute_sensitivity(df)

    print("Inputs ranked by influence on mechanical recycling's advantage")
    print("(green = higher value helps mechanical, red = higher value helps chemical)\n")
    print(sens.to_string(index=False, float_format=lambda x: f"{x:+.2f}"))

    csv_path = os.path.join(TABLES_DIR, "sensitivity.csv")
    sens.to_csv(csv_path, index=False)
    print(f"\nSaved: {csv_path}")

    plot_sensitivity(sens)