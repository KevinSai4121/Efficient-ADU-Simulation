class GISAnalyzer:
    """
    This module analyzes zoning constraints and environmental factors to determine 
    whether an ADU can be placed on a property.
    """

    def __init__(self):
        # Example zoning constraints (modifiable for real-world data)
        self.zoning_restrictions = {
            "minimum_lot_size": 4000,  # Minimum lot size in square feet for ADU approval
            "max_slope": 15,  # Maximum slope (degrees) for ADU construction
            "flood_zone_restriction": True  # Flag to reject ADUs in flood zones
        }

    def analyze_zoning_constraints(self, property_data):
        """
        Checks if the property meets zoning requirements.

        Parameters:
        - property_data (dict): Contains details about property size, slope, and zoning compliance.

        Returns:
        - bool: True if ADU placement is allowed, False otherwise.
        """
        lot_size = property_data.get("size", 0)
        slope = property_data.get("slope", 0)
        zoning_compliance = property_data.get("zoning_compliance", True)

        # Check lot size
        if lot_size < self.zoning_restrictions["minimum_lot_size"]:
            print("Zoning Restriction: Lot size is too small for ADU placement.")
            return False

        # Check slope restriction
        if slope > self.zoning_restrictions["max_slope"]:
            print("Zoning Restriction: Slope exceeds the allowable limit for ADU construction.")
            return False

        # Check flood zone restrictions
        if self.zoning_restrictions["flood_zone_restriction"] and not zoning_compliance:
            print("Zoning Restriction: Property is located in a restricted flood zone.")
            return False

        return True

    def evaluate_sunlight_exposure(self, property_data):
        """
        Estimates sunlight exposure based on geospatial data.

        Parameters:
        - property_data (dict): Contains latitude, longitude, and any environmental constraints.

        Returns:
        - str: Sunlight exposure category (High, Medium, Low).
        """
        latitude = property_data.get("latitude", 34.0)  # Default: Georgia, USA
        longitude = property_data.get("longitude", -84.0)
        tree_cover_percentage = property_data.get("tree_cover", 20)  # Default 20% shade

        # Basic sunlight exposure evaluation
        if tree_cover_percentage > 50:
            return "Low"
        elif 20 <= tree_cover_percentage <= 50:
            return "Medium"
        else:
            return "High"

# Example usage
if __name__ == "__main__":
    gis_analyzer = GISAnalyzer()

    # Sample property data
    property_data = {
        "size": 5000,  # Square feet
        "slope": 5,  # Degrees
        "zoning_compliance": True,
        "latitude": 34.05,
        "longitude": -118.25,
        "tree_cover": 30
    }

    # Run zoning analysis
    zoning_result = gis_analyzer.analyze_zoning_constraints(property_data)
    print(f"Zoning Approval: {zoning_result}")

    # Run sunlight exposure analysis
    sunlight_exposure = gis_analyzer.evaluate_sunlight_exposure(property_data)
    print(f"Sunlight Exposure: {sunlight_exposure}")
