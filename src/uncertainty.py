"""
uncertainty.py
--------------
Monte Carlo uncertainty analysis for the PET end-of-life pathway model.
"""

import random
import statistics
from model import mechanical_recycling, chemical_recycling, energy_recovery, landfill
from parameters import UNCERTAINTY_RANGES

N_SIMULATIONS = 5000


def sample(range_tuple):
    low, high = range_tuple
    return random.uniform(low, high)


def sample_params(pathway_name):
    return {k: sample(v) for k, v in UNCERTAINTY_RANGES[pathway_name].items()}


def run_simulation():
    results = {
        "Mechanical Recycling": [],
        "Chemical Recycling": [],
        "Energy Recovery": [],
        "Landfill": [],
    }

    win_counts = {name: 0 for name in results}

    for _ in range(N_SIMULATIONS):
        mech_params = sample_params("mechanical")
        chem_params = sample_params("chemical")
        energy_params = sample_params("energy")
        landfill_params = sample_params("landfill")

        run_results = {
            "Mechanical Recycling": mechanical_recycling(mech_params),
            "Chemical Recycling": chemical_recycling(chem_params),
            "Energy Recovery": energy_recovery(energy_params),
            "Landfill": landfill(landfill_params),
        }

        for name, value in run_results.items():
            results[name].append(value)

        winner = min(run_results, key=run_results.get)
        win_counts[winner] += 1

    return results, win_counts


def summarize(results, win_counts, n_simulations):
    print(f"Monte Carlo results over {n_simulations} simulations\n")
    print(f"{'Pathway':<22}{'Mean':>10}{'Std Dev':>10}{'Min':>10}{'Max':>10}{'Win %':>10}")
    print("-" * 72)

    for name, values in results.items():
        mean = statistics.mean(values)
        stdev = statistics.stdev(values)
        vmin = min(values)
        vmax = max(values)
        win_pct = 100 * win_counts[name] / n_simulations
        print(f"{name:<22}{mean:>10.1f}{stdev:>10.1f}{vmin:>10.1f}{vmax:>10.1f}{win_pct:>9.1f}%")
        
