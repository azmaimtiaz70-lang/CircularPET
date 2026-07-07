"""
parameters.py
-------------
Baseline parameters and uncertainty ranges for PET circularity model.
"""

FUNCTIONAL_UNIT_KG = 1000  # 1 metric ton of post-consumer PET waste

BASELINE_PARAMS = {
    "mechanical": {
        "collection_rate": 0.75,
        "sorting_yield": 0.90,
        "process_yield": 0.92,
        "rpet_emission_factor": 0.45,
        "virgin_emission_factor": 2.15,
        "landfill_emission_factor": 0.05,
    },
    "chemical": {
        "collection_rate": 0.75,
        "process_yield": 0.85,
        "chemical_emission_factor": 1.20,
        "virgin_emission_factor": 2.15,
        "landfill_emission_factor": 0.05,
    },
    "energy": {
        "combustion_emission_factor": 2.50,
        "energy_recovered_per_kg": 20.0,
        "grid_emission_factor": 0.10,
    },
    "landfill": {
        "landfill_emission_factor": 0.05,
    },
}

UNCERTAINTY_RANGES = {
    "mechanical": {
        "collection_rate": (0.60, 0.85),
        "sorting_yield": (0.80, 0.95),
        "process_yield": (0.85, 0.95),
        "rpet_emission_factor": (0.35, 0.60),
        "virgin_emission_factor": (1.90, 2.40),
        "landfill_emission_factor": (0.03, 0.08),
    },
    "chemical": {
        "collection_rate": (0.60, 0.85),
        "process_yield": (0.70, 0.90),
        "chemical_emission_factor": (0.80, 1.80),
        "virgin_emission_factor": (1.90, 2.40),
        "landfill_emission_factor": (0.03, 0.08),
    },
    "energy": {
        "combustion_emission_factor": (2.00, 3.00),
        "energy_recovered_per_kg": (15.0, 25.0),
        "grid_emission_factor": (0.05, 0.15),
    },
    "landfill": {
        "landfill_emission_factor": (0.03, 0.08),
    },
}
