class EnergyModel:
    """
    This module computes the energy efficiency of an ADU based on its materials, insulation,
    and HVAC system. It provides an energy efficiency score on a scale from 0 to 1.
    """

    def __init__(self):
        # Base energy consumption per square foot (kWh per day)
        self.base_energy_per_sqft = 0.05  

        # Material energy efficiency ratings (higher is better)
        self.material_efficiency = {
            "wood_frame": 0.75,
            "steel_frame": 0.80,
            "concrete": 0.85
        }

        # HVAC system efficiency ratings (higher is better)
        self.hvac_efficiency = {
            "standard": 0.70,
            "high_efficiency": 0.90
        }

        # Insulation efficiency multipliers (higher = better insulation, lower energy use)
        self.insulation_efficiency = {
            "standard": 1.0,
            "high_efficiency": 0.85,
            "passive_house": 0.70
        }

    def compute_efficiency(self, design):
        """
        Computes the energy efficiency of an ADU based on its design parameters.

        Parameters:
        - design (dict): ADU design details including floor area, materials, HVAC, and insulation.

        Returns:
        - float: An energy efficiency score between 0 and 1.
        """
        floor_area = design.get("floor_area", 600)  # Default 600 sq. ft.
        material = design.get("materials", "wood_frame")
        hvac = design.get("hvac", "standard")
        insulation = design.get("insulation", "standard")

        # Get efficiency values (defaulting to lowest if missing)
        material_score = self.material_efficiency.get(material, 0.75)
        hvac_score = self.hvac_efficiency.get(hvac, 0.70)
        insulation_multiplier = self.insulation_efficiency.get(insulation, 1.0)

        # Compute total energy efficiency score (higher is better)
        efficiency_score = (material_score + hvac_score) / 2

        # Adjust efficiency based on insulation quality
        efficiency_score *= insulation_multiplier

        return round(efficiency_score, 2)

    def estimate_daily_energy_usage(self, design):
        """
        Estimates the daily energy consumption of an ADU.

        Parameters:
        - design (dict): ADU design details including floor area, materials, HVAC, and insulation.

        Returns:
        - float: Estimated energy usage in kWh per day.
        """
        floor_area = design.get("floor_area", 600)  # Default 600 sq. ft.
        insulation = design.get("insulation", "standard")

        # Get insulation multiplier
        insulation_multiplier = self.insulation_efficiency.get(insulation, 1.0)

        # Calculate daily energy usage
        daily_energy_usage = self.base_energy_per_sqft * floor_area * insulation_multiplier
        return round(daily_energy_usage, 2)

# Example usage
if __name__ == "__main__":
    energy_model = EnergyModel()

    # Sample ADU designs
    adu_designs = [
        {"floor_area": 600, "materials": "wood_frame", "hvac": "standard", "insulation": "standard"},
        {"floor_area": 750, "materials": "steel_frame", "hvac": "high_efficiency", "insulation": "high_efficiency"},
        {"floor_area": 900, "materials": "concrete", "hvac": "high_efficiency", "insulation": "passive_house"},
    ]

    for design in adu_designs:
        efficiency = energy_model.compute_efficiency(design)
        energy_usage = energy_model.estimate_daily_energy_usage(design)
        print(f"ADU Design: {design}")
        print(f"  - Energy Efficiency Score: {efficiency}")
        print(f"  - Estimated Daily Energy Usage: {energy_usage} kWh/day\n")
