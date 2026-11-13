"""
parameters.py
-------------
Baseline parameters and uncertainty ranges for PET circularity model.
"""

FUNCTIONAL_UNIT_KG = 1000  # 1 metric ton of post-consumer PET waste

BASELINE_PARAMS = {
    "mechanical": {
        "displacement_ratio": 0.85,
        "collection_rate": 0.75,
        "sorting_yield": 0.90,
        "process_yield": 0.92,
        "rpet_emission_factor": 0.45,
        "virgin_emission_factor": 2.15,
        "landfill_emission_factor": 0.05,
    },
    "chemical": {
        "displacement_ratio": 0.95,
        "collection_rate": 0.75,
        "process_yield": 0.85,
        "chemical_emission_factor": 1.20,
        "virgin_emission_factor": 2.15,
        "landfill_emission_factor": 0.05,
    },
    "energy": {
        "combustion_emission_factor": 2.15,
        "heating_value_mj_per_kg": 23.0,
        "electrical_efficiency": 0.22,
        "grid_emission_factor": 0.10,
    },
    "landfill": {
        "landfill_emission_factor": 0.05,
    },
}

UNCERTAINTY_RANGES = {
    "mechanical": {
        "displacement_ratio": (0.50, 1.00),
        "collection_rate": (0.60, 0.85),
        "sorting_yield": (0.80, 0.95),
        "process_yield": (0.85, 0.95),
        "rpet_emission_factor": (0.35, 0.60),
        "virgin_emission_factor": (1.90, 2.40),
        "landfill_emission_factor": (0.03, 0.08),
    },
    "chemical": {
        "displacement_ratio": (0.90, 1.00),
        "collection_rate": (0.60, 0.85),
        "process_yield": (0.70, 0.90),
        "chemical_emission_factor": (0.80, 1.80),
        "virgin_emission_factor": (1.90, 2.40),
        "landfill_emission_factor": (0.03, 0.08),
    },
    "energy": {
        "combustion_emission_factor": (2.00, 2.29),
        "heating_value_mj_per_kg": (21.8, 24.4),
        "electrical_efficiency": (0.15, 0.30),
        "grid_emission_factor": (0.05, 0.15),
    },
    "landfill": {
        "landfill_emission_factor": (0.03, 0.08),
    },
}