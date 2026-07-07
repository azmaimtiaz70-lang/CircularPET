# Final Report

## Introduction

This project compares four end-of-life pathways for post-consumer PET waste: mechanical recycling, chemical recycling, energy recovery, and landfill. The goal is to estimate the net greenhouse gas impact of each pathway and test how stable the ranking is under uncertainty.

## Methods

The model uses a functional unit of 1 metric ton of post-consumer PET waste. A baseline pathway model was implemented in `src/model.py`, and uncertainty was explored using Monte Carlo simulation in `src/uncertainty.py` with 5000 runs. Summary statistics were saved to CSV, and results were visualized using box plots and win-rate charts.

## Results

The current simulation shows mechanical recycling with the lowest mean GHG impact and the highest win rate. Chemical recycling is generally the second-best option, while energy recovery and landfill perform worse under the present assumptions. The results are shown in `results/figures/box_comparison.png` and `results/figures/win_percentage.png`.

## Discussion

Mechanical recycling performs best mainly because the model gives it a large credit for avoided virgin PET production. Energy recovery shows high uncertainty because its outcome depends strongly on combustion emissions and electricity displacement assumptions. These results should be treated as a first-pass estimate rather than a final literature benchmark.

## Conclusion

Under the current assumptions, mechanical recycling is the best-performing PET end-of-life pathway. However, the ranking remains sensitive to parameter choices, so the model should be refined with more detailed literature values and region-specific data in future work.
