# EcoCompAI

A Python project for comparing PET end-of-life pathways using a baseline model and Monte Carlo uncertainty analysis.

## Overview

This repository compares different PET waste management pathways, including mechanical recycling, chemical recycling, energy recovery, and landfill. The model estimates net greenhouse gas impact per 1 metric ton of PET waste. It also tests how sensitive the ranking is under uncertainty.

## Methods

The project uses:
- a baseline impact model in `src/model.py`,
- uncertainty ranges and Monte Carlo simulation in `src/uncertainty.py`,
- plots in `src/plots.py`,
- and summary outputs saved in `results/`.

## Folder Structure

- `data/` — input data and parameter files.
- `docs/` — methodology notes.
- `notebooks/` — exploration notebooks.
- `results/` — figures and tables.
- `reports/` — final write-ups.
- `src/` — Python code.

## Results

The current simulation shows mechanical recycling as the lowest-impact pathway most of the time. The figures are saved as:
- `results/figures/box_comparison.png`
- `results/figures/win_percentage.png`

## How to Run

1. Run `python src/uncertainty.py`
2. Run `python src/plots.py`
3. Check the `results/tables/` and `results/figures/` folders.