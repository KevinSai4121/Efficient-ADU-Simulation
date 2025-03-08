class CostEstimator:
    """
    This module estimates the total construction cost of an ADU based on materials, labor,
    and size. It applies a cost model that considers material type, labor costs, and floor area.
    """

    def __init__(self):
        # Base cost per square foot for ADU construction (adjustable based on market trends)
        self.base_cost_per_sqft = 100  

        # Material cost multipliers
        self.material_cost = {
            "wood_frame": 1.0,
            "steel_frame": 1.2,
            "concrete": 1.5
        }

        # HVAC system cost multipliers
        self.hvac_cost = {
            "standard": 1.0,
            "high_efficiency": 1.1
        }

        # Labor cost per square foot
        self.labor_cost_per_sqft = 50  

    def estimate_total_cost(self, design):
        """
        Estimates the total cost of an ADU construction project.

        Parameters:
        - design (dict): ADU design parameters, including "floor_area", "materials", and "hvac".

        Returns:
        - float: Total estimated cost in USD.
        """
        floor_area = design.get("floor_area", 600)  # Default size if not specified
        material_type = design.get("materials", "wood_frame")
        hvac_type = design.get("hvac", "standard")

        # Get multipliers (defaulting to 1.0 if unknown)
        material_multiplier = self.material_cost.get(material_type, 1.0)
        hvac_multiplier = self.hvac_cost.get(hvac_type, 1.0)

        # Calculate costs
        base_cost = floor_area * self.base_cost_per_sqft * material_multiplier
        labor_cost = floor_area * self.labor_cost_per_sqft
        hvac_system_cost = base_cost * hvac_multiplier

        # Total cost
        total_cost = base_cost + labor_cost + hvac_system_cost
        return round(total_cost, 2)

# Example usage
if __name__ == "__main__":
    cost_estimator = CostEstimator()

    # Sample ADU designs
    adu_designs = [
        {"floor_area": 600, "materials": "wood_frame", "hvac": "standard"},
        {"floor_area": 750, "materials": "steel_frame", "hvac": "high_efficiency"},
        {"floor_area": 900, "materials": "concrete", "hvac": "high_efficiency"},
    ]

    for design in adu_designs:
        cost = cost_estimator.estimate_total_cost(design)
        print(f"Estimated Cost for ADU ({design}): ${cost:,.2f}")
