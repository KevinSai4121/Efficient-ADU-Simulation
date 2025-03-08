class PropertyModel:
    """
    This module represents a property and validates whether an ADU can be placed on it
    based on zoning regulations, lot size, and slope conditions.
    """

    def __init__(self, property_data):
        """
        Initializes the property with relevant constraints.

        Parameters:
        - property_data (dict): Contains property size, slope, and zoning compliance status.
        """
        self.size = property_data.get("size", 5000)  # Default 5000 sq. ft.
        self.slope = property_data.get("slope", 5)  # Default 5 degrees
        self.zoning_compliance = property_data.get("zoning_compliance", True)

        # Define zoning requirements
        self.minimum_lot_size = 4000  # Minimum required lot size (sq. ft.)
        self.max_slope = 15  # Maximum allowable slope for ADU construction (degrees)

    def get_constraints(self):
        """
        Returns the property constraints as a dictionary.

        Returns:
        - dict: Property constraints including lot size, slope, and zoning compliance.
        """
        return {
            "size": self.size,
            "slope": self.slope,
            "zoning_compliance": self.zoning_compliance
        }

    def is_adu_allowed(self):
        """
        Determines if an ADU can be placed on the property based on constraints.

        Returns:
        - bool: True if ADU placement is allowed, False otherwise.
        """
        if self.size < self.minimum_lot_size:
            print("Zoning Restriction: Lot size is too small for ADU placement.")
            return False

        if self.slope > self.max_slope:
            print("Zoning Restriction: Slope exceeds allowable limit for ADU construction.")
            return False

        if not self.zoning_compliance:
            print("Zoning Restriction: Property is not compliant with zoning laws.")
            return False

        return True

# Example usage
if __name__ == "__main__":
    properties = [
        {"size": 5000, "slope": 5, "zoning_compliance": True},
        {"size": 3000, "slope": 10, "zoning_compliance": True},  # Lot too small
        {"size": 6000, "slope": 20, "zoning_compliance": True},  # Slope too high
        {"size": 4500, "slope": 8, "zoning_compliance": False},  # Fails zoning
    ]

    for property_data in properties:
        property_model = PropertyModel(property_data)
        print(f"Property Constraints: {property_model.get_constraints()}")
        print(f"ADU Allowed: {property_model.is_adu_allowed()}\n")
