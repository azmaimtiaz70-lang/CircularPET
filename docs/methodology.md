# Methodology

## System Boundary

The model compares four end-of-life pathways for 1 metric ton of post-consumer PET waste: mechanical recycling, chemical recycling, energy recovery, and landfill. The output is net greenhouse gas impact in kg CO2-equivalent per functional unit.

## Baseline Model

The baseline model is implemented in `src/model.py`. Each pathway is represented as a function that receives a dictionary of parameters and returns a single net GHG impact value. For recycling pathways, the model includes process emissions and avoided virgin PET emissions.

## Uncertainty Analysis

The uncertainty analysis is implemented in `src/uncertainty.py`. It uses Monte Carlo simulation with 5000 runs. In each run, pathway parameters are sampled from predefined ranges, and the model is evaluated repeatedly to estimate the distribution of outcomes.

## Outputs

The analysis produces a CSV summary table in `results/tables/uncertainty_summary.csv` and two figures in `results/figures/`: `box_comparison.png` and `win_percentage.png`.

## Limitations

The current parameter values are placeholder estimates and should be refined with a fuller literature review. The model is intended as a transparent starting point for comparing PET end-of-life pathways.

