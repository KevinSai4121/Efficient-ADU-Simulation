import numpy as np

class OptimizationModule:
    """
    This module identifies the optimal ADU design based on cost, energy efficiency, and zoning compliance.
    It evaluates multiple designs and selects the one that balances affordability and efficiency.
    """

    def __init__(self):
        pass

    def evaluate_design(self, design):
        """
        Scores an ADU design based on cost and energy efficiency.

        Parameters:
        - design (dict): Dictionary containing ADU specifications (floor_area, materials, hvac).

        Returns:
        - float: A score representing the design's efficiency (higher is better).
        """
        cost = self.estimate_cost(design)
        efficiency = self.estimate_energy_efficiency(design)

        # Normalize cost and efficiency to a 0-1 scale
        cost_score = 1 / (1 + cost / 100000)  # Assume $100,000 as baseline cost
        efficiency_score = efficiency  # Already in a 0-1 range

        # Weighted scoring system (adjust weights as needed)
        total_score = (0.6 * efficiency_score) + (0.4 * cost_score)

        return total_score

    def find_optimal_design(self, designs):
        """
        Selects the best ADU design from a list based on optimization criteria.

        Parameters:
        - designs (list): A list of dictionaries, each representing an ADU design.

        Returns:
        - dict: The optimal ADU design.
        """
        if not designs:
            return None

        best_design = max(designs, key=self.evaluate_design)
        return best_design

    def estimate_cost(self, design):
        """
        Estimates the total construction cost of an ADU.

        Parameters:
        - design (dict): Dictionary containing ADU details.

        Returns:
        - float: Estimated cost in USD.
        """
        base_cost = 50000  # Base construction cost
        material_multiplier = {"wood_frame": 1.0, "steel_frame": 1.2, "concrete": 1.5}
        hvac_multiplier = {"standard": 1.0, "high_efficiency": 1.1}

        material_factor = material_multiplier.get(design.get("materials", "wood_frame"), 1.0)
        hvac_factor = hvac_multiplier.get(design.get("hvac", "standard"), 1.0)

        total_cost = base_cost * material_factor * hvac_factor + (design.get("floor_area", 600) * 50)
        return total_cost

    def estimate_energy_efficiency(self, design):
        """
        Estimates the energy efficiency of an ADU based on HVAC system and materials.

        Parameters:
        - design (dict): Dictionary containing ADU details.

        Returns:
        - float: Energy efficiency score (0-1 scale).
        """
        hvac_efficiency = {"standard": 0.7, "high_efficiency": 0.9}
        material_efficiency = {"wood_frame": 0.75, "steel_frame": 0.8, "concrete": 0.85}

        hvac_score = hvac_efficiency.get(design.get("hvac", "standard"), 0.7)
        material_score = material_efficiency.get(design.get("materials", "wood_frame"), 0.75)

        return (hvac_score + material_score) / 2

# Example usage
if __name__ == "__main__":
    optimizer = OptimizationModule()

    designs = [
        {"floor_area": 600, "materials": "wood_frame", "hvac": "standard"},
        {"floor_area": 700, "materials": "steel_frame", "hvac": "high_efficiency"},
        {"floor_area": 800, "materials": "concrete", "hvac": "high_efficiency"},
    ]

    best_design = optimizer.find_optimal_design(designs)
    print("Best ADU Design:", best_design)
