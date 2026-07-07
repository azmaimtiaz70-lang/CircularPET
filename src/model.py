"""
model.py
--------
Baseline decision model for comparing PET end-of-life (EOL) pathways.

Functional unit: 1 metric ton (1000 kg) of post-consumer PET waste.
Output: net GHG impact in kg CO2-equivalent per functional unit.

STARTING VALUES: The numbers below are rough anchors pulled from published
LCA literature (ALPLA/PET Recycling Team, NAPCOR, Ncube & Borodin, Meys et al.).
They are NOT final — different studies report different values depending on
system boundary, region, and methodology. Treat these as Week 1-2 placeholders
to refine once you do your own literature pass. That variation is exactly what
the uncertainty analysis (later) is meant to capture.

Each pathway function takes a dict of parameters and returns one number:
kg CO2-eq per ton of waste processed (LOWER = better).
"""

FUNCTIONAL_UNIT_KG = 1000  # 1 ton of post-consumer PET waste


def mechanical_recycling(params):
    """
    Steps: collect -> sort -> wash/shred/melt -> reform into rPET pellets.
    rPET displaces virgin PET production (this is the 'credit').

    params expected:
        collection_rate      : fraction of waste actually collected (0-1)
        sorting_yield         : fraction surviving sorting (0-1)
        process_yield         : fraction surviving reprocessing (0-1)
        rpet_emission_factor  : kg CO2e per kg rPET produced
        virgin_emission_factor: kg CO2e per kg virgin PET (credit avoided)
    """
    material_recovered = (
        FUNCTIONAL_UNIT_KG
        * params["collection_rate"]
        * params["sorting_yield"]
        * params["process_yield"]
    )
    lost_material = FUNCTIONAL_UNIT_KG - material_recovered

    # emissions from producing the recovered material as rPET
    process_emissions = material_recovered * params["rpet_emission_factor"]

    # credit: recovered material displaces virgin PET that would've been made
    avoided_emissions = material_recovered * params["virgin_emission_factor"]

    # material that couldn't be recovered is assumed landfilled (simple assumption)
    lost_material_emissions = lost_material * params.get("landfill_emission_factor", 0.05)

    net_impact = process_emissions - avoided_emissions + lost_material_emissions
    return net_impact


def chemical_recycling(params):
    """
    Steps: collect -> depolymerize (higher energy than mechanical) -> resynthesize.
    Handles lower-quality/contaminated waste better than mechanical, but usually
    more energy-intensive per kg processed.

    params expected:
        collection_rate        : fraction collected (0-1)
        process_yield           : fraction converted back to usable monomer/resin (0-1)
        chemical_emission_factor: kg CO2e per kg output (higher than mechanical)
        virgin_emission_factor  : kg CO2e per kg virgin PET (credit avoided)
    """
    material_recovered = (
        FUNCTIONAL_UNIT_KG
        * params["collection_rate"]
        * params["process_yield"]
    )
    lost_material = FUNCTIONAL_UNIT_KG - material_recovered

    process_emissions = material_recovered * params["chemical_emission_factor"]
    avoided_emissions = material_recovered * params["virgin_emission_factor"]
    lost_material_emissions = lost_material * params.get("landfill_emission_factor", 0.05)

    net_impact = process_emissions - avoided_emissions + lost_material_emissions
    return net_impact


def energy_recovery(params):
    """
    Incineration with energy capture. No material is recycled; all of it is
    burned, but the energy generated offsets some grid electricity (credit).

    params expected:
        combustion_emission_factor: kg CO2e per kg PET incinerated
        energy_recovered_per_kg    : MJ of usable energy recovered per kg burned
        grid_emission_factor       : kg CO2e per MJ of grid electricity displaced
    """
    combustion_emissions = FUNCTIONAL_UNIT_KG * params["combustion_emission_factor"]
    energy_generated = FUNCTIONAL_UNIT_KG * params["energy_recovered_per_kg"]
    avoided_emissions = energy_generated * params["grid_emission_factor"]

    net_impact = combustion_emissions - avoided_emissions
    return net_impact


def landfill(params):
    """
    Simplest pathway: no processing, no credit. Just decomposition emissions
    (PET is slow to decompose but transport/handling still has a footprint).

    params expected:
        landfill_emission_factor: kg CO2e per kg landfilled
    """
    return FUNCTIONAL_UNIT_KG * params["landfill_emission_factor"]


if __name__ == "__main__":
    # --- Rough starting parameters (literature-anchored placeholders) ---
    mech_params = {
        "collection_rate": 0.75,
        "sorting_yield": 0.90,
        "process_yield": 0.92,
        "rpet_emission_factor": 0.45,     # ALPLA study
        "virgin_emission_factor": 2.15,   # ALPLA study
        "landfill_emission_factor": 0.05,
    }

    chem_params = {
        "collection_rate": 0.75,
        "process_yield": 0.85,
        "chemical_emission_factor": 1.20,  # placeholder, refine with your own sources
        "virgin_emission_factor": 2.15,
        "landfill_emission_factor": 0.05,
    }

    energy_params = {
        "combustion_emission_factor": 2.5,   # placeholder
        "energy_recovered_per_kg": 20,       # MJ/kg, rough for PET
        "grid_emission_factor": 0.10,        # kg CO2e/MJ, adjust for region
    }

    landfill_params = {
        "landfill_emission_factor": 0.05,
    }

    results = {
        "Mechanical Recycling": mechanical_recycling(mech_params),
        "Chemical Recycling": chemical_recycling(chem_params),
        "Energy Recovery": energy_recovery(energy_params),
        "Landfill": landfill(landfill_params),
    }

    print("Net GHG impact per 1 ton PET waste (kg CO2-eq):\n")
    for pathway, impact in sorted(results.items(), key=lambda x: x[1]):
        print(f"  {pathway:22s}: {impact:8.1f}")
