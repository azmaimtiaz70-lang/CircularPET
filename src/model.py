"""
model.py
--------
Baseline decision model for comparing PET end-of-life (EOL) pathways.
"""

from parameters import FUNCTIONAL_UNIT_KG


def mechanical_recycling(params):
    material_recovered = (
        FUNCTIONAL_UNIT_KG
        * params["collection_rate"]
        * params["sorting_yield"]
        * params["process_yield"]
    )
    lost_material = FUNCTIONAL_UNIT_KG - material_recovered
    process_emissions = material_recovered * params["rpet_emission_factor"]
    avoided_emissions = (
        material_recovered
        * params["displacement_ratio"]
        * params["virgin_emission_factor"]
    )
    lost_material_emissions = lost_material * params.get("landfill_emission_factor", 0.05)
    return process_emissions - avoided_emissions + lost_material_emissions


def chemical_recycling(params):
    material_recovered = (
        FUNCTIONAL_UNIT_KG
        * params["collection_rate"]
        * params["process_yield"]
    )
    lost_material = FUNCTIONAL_UNIT_KG - material_recovered
    process_emissions = material_recovered * params["chemical_emission_factor"]
    avoided_emissions = (
        material_recovered
        * params["displacement_ratio"]
        * params["virgin_emission_factor"]
    )
    lost_material_emissions = lost_material * params.get("landfill_emission_factor", 0.05)
    return process_emissions - avoided_emissions + lost_material_emissions


def energy_recovery(params):
    combustion_emissions = FUNCTIONAL_UNIT_KG * params["combustion_emission_factor"]
    energy_content = FUNCTIONAL_UNIT_KG * params["heating_value_mj_per_kg"]
    electricity_generated = energy_content * params["electrical_efficiency"]
    avoided_emissions = electricity_generated * params["grid_emission_factor"]
    return combustion_emissions - avoided_emissions


def landfill(params):
    return FUNCTIONAL_UNIT_KG * params["landfill_emission_factor"]