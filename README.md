# CircularPET

A Python project for comparing PET end-of-life pathways using a baseline model and Monte Carlo uncertainty analysis.

## Overview

This repository compares four PET waste management pathways: mechanical recycling, chemical recycling, energy recovery and landfill. The model estimates net greenhouse gas (GHG) impact per 1 metric ton of PET waste, in kg CO2-eq. A lower (more negative) value is better. It also tests how stable the ranking is when the inputs are uncertain, and which inputs matter most.

## Methods

- `src/model.py`: baseline impact model, one formula per pathway.
- `src/parameters.py`: uncertainty ranges for every input.
- `src/uncertainty.py`: Monte Carlo simulation (5,000 runs, fixed random seed 42, so results are reproducible).
- `src/plots.py`: box plot and win-percentage figures.
- `src/sensitivity.py`: rank-correlation sensitivity analysis.
- `results/`: saved tables and figures.

In each run, every input is drawn at random from its range. Inputs that are physically the same quantity (collection rate, virgin PET emission factor, landfill emission factor) are drawn once per run and shared across pathways. The pathway with the lowest net impact in that run is counted as the winner.

Recycling credits depend on a displacement ratio, which is how much virgin PET one kg of recycled PET actually replaces. Energy recovery credit is calculated from PET heating value and the plant's electrical efficiency.

## Results

| Pathway | Mean (kg CO2-eq/t) | Win % |
|---|---|---|
| Mechanical recycling | -626.7 | 78.4% |
| Chemical recycling | -406.3 | 21.6% |
| Energy recovery | 1627.4 | 0.0% |
| Landfill | 55.2 | 0.0% |

Both recycling routes clearly beat energy recovery and landfill. Mechanical recycling wins most runs, but chemical recycling wins about one run in five.

The choice between the two recycling routes is driven mainly by two inputs: the displacement ratio of mechanically recycled PET and the emission factor of the chemical process (see `results/figures/sensitivity.png`). Collection rate, sorting yield and landfill factor have little effect on that choice.

Figures are in `results/figures/`: `box_comparison.png`, `win_percentage.png`, `sensitivity.png`.

## Assumptions and limitations

- Only GHG is modelled. Cost, contamination, regional differences and other environmental impacts (such as land use or microplastic leakage from landfill) are not included.
- Energy recovery looks worse than landfill because burning PET releases its fossil carbon as CO2, while landfilled PET stays largely inert. This is a GHG-only result.
- Displacement ratio (0.5 to 1.0 for mechanical, 0.9 to 1.0 for chemical), PET heating value (21.8 to 24.4 MJ/kg) and plant electrical efficiency (15% to 30%) are based on published values. The 0.5 lower bound on the mechanical displacement ratio is a judgment call.
- Other input ranges are working assumptions and have not been validated against site-specific data.
- Sensitivity results depend on how wide each range is set, so inputs with wider ranges tend to rank higher.

## Folder Structure

- `data/`: input data and parameter files
- `docs/`: methodology notes
- `notebooks/`: exploration notebooks
- `results/`: figures and tables
- `reports/`: final write-ups
- `src/`: Python code

## How to Run

1. Install the libraries: `pip install matplotlib pandas`
2. On Windows, double-click `run.bat` (or run the three scripts below yourself).
3. `python src/uncertainty.py`
4. `python src/plots.py`
5. `python src/sensitivity.py`
6. Check the `results/tables/` and `results/figures/` folders.