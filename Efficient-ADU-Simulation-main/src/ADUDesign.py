class ADUDesign:
    """
    This module handles the design components of an Accessory Dwelling Unit (ADU),
    including floor area, materials, energy efficiency factors, and livable space calculations.
    """

    def __init__(self, design_data):
        """
        Initializes an ADU design with the given parameters.

        Parameters:
        - design_data (dict): Contains floor area, materials, and HVAC system type.
        """
        self.floor_area = design_data.get("floor_area", 600)  # Default: 600 sq. ft.
        self.materials = design_data.get("materials", "wood_frame")
        self.hvac = design_data.get("hvac", "standard")
        self.insulation = design_data.get("insulation", "standard")

        # Space efficiency multiplier (accounts for walls, storage, etc.)
        self.space_efficiency = {
            "wood_frame": 0.85,
            "steel_frame": 0.80,
            "concrete": 0.75
        }

    def calculate_livable_space(self):
        """
        Calculates the livable space within the ADU after accounting for structural elements.

        Returns:
        - float: Livable area in square feet.
        """
        efficiency_factor = self.space_efficiency.get(self.materials, 0.85)
        livable_area = self.floor_area * efficiency_factor
        return round(livable_area, 2)

    def get_design_details(self):
        """
        Returns the details of the ADU design as a dictionary.

        Returns:
        - dict: ADU design specifications.
        """
        return {
            "floor_area": self.floor_area,
            "materials": self.materials,
            "hvac": self.hvac,
            "insulation": self.insulation,
            "livable_space": self.calculate_livable_space()
        }

# Example usage
if __name__ == "__main__":
    adu_designs = [
        {"floor_area": 600, "materials": "wood_frame", "hvac": "standard", "insulation": "standard"},
        {"floor_area": 750, "materials": "steel_frame", "hvac": "high_efficiency", "insulation": "high_efficiency"},
        {"floor_area": 900, "materials": "concrete", "hvac": "high_efficiency", "insulation": "passive_house"},
    ]

    for design in adu_designs:
        adu = ADUDesign(design)
        details = adu.get_design_details()
        print(f"ADU Design Details: {details}\n")
