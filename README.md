# CircularPET

A Python project for comparing PET end-of-life pathways using a baseline model and Monte Carlo uncertainty analysis.

## Overview

This repository compares four PET waste management pathways: mechanical recycling, chemical recycling, energy recovery and landfill. The model estimates net greenhouse gas (GHG) impact per 1 metric ton of PET waste, in kg CO2-eq. A lower (more negative) value is better. It also tests how stable the ranking is when the inputs are uncertain.

## Methods

- `src/model.py`: baseline impact model, one formula per pathway.
- `src/parameters.py`: uncertainty ranges for every input.
- `src/uncertainty.py`: Monte Carlo simulation (5,000 runs, fixed random seed 42, so results are reproducible).
- `src/plots.py`: figures.
- `results/`: saved tables and figures.

In each run, every input is drawn at random from its range. Inputs that are physically the same quantity (collection rate, virgin PET emission factor, landfill emission factor) are drawn once per run and shared across pathways. The pathway with the lowest net impact in that run is counted as the winner.

## Results

| Pathway | Mean (kg CO2-eq/t) | Win % |
|---|---|---|
| Mechanical recycling | -932.5 | 92.9% |
| Chemical recycling | -471.0 | 0.2% |
| Energy recovery | 158.9 | 7.0% |
| Landfill | 55.1 | 0.0% |

Mechanical recycling has the lowest impact in most runs. Figures are saved in `results/figures/` (`box_comparison.png`, `win_percentage.png`).

## Assumptions and limitations

- Recycled PET is assumed to replace virgin PET 1:1, which gives a large avoided-emissions credit. The ranking depends strongly on this.
- The energy recovery credit assumes a fixed amount of recovered energy per kg and a grid emission factor, and may be generous.
- Only GHG is modelled. Cost, contamination and regional differences are not included.
- Input ranges are literature-style assumptions and have not been validated against site-specific data.

## Folder Structure

- `data/`: input data and parameter files
- `docs/`: methodology notes
- `notebooks/`: exploration notebooks
- `results/`: figures and tables
- `reports/`: final write-ups
- `src/`: Python code

## How to Run

1. Install the libraries: `pip install matplotlib pandas`
2. Run `python src/uncertainty.py`
3. Run `python src/plots.py`
4. Check the `results/tables/` and `results/figures/` folders.