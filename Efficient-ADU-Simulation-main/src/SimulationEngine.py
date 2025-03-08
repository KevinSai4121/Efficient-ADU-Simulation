from src.PropertyModel import PropertyModel
from src.ADUDesign import ADUDesign
from src.EnergyModel import EnergyModel
from src.CostEstimator import CostEstimator
from src.GISAnalyzer import GISAnalyzer
from src.OptimizationModule import OptimizationModule

class SimulationEngine:
    """
    This module runs the ADU simulation, integrating property constraints, energy efficiency,
    construction cost estimation, GIS analysis, and optimization.
    """

    def __init__(self):
        self.energy_model = EnergyModel()
        self.cost_estimator = CostEstimator()
        self.gis_analyzer = GISAnalyzer()
        self.optimization_module = OptimizationModule()

    def run_simulation(self, property_data, adu_designs):
        """
        Runs the simulation for ADU feasibility.

        Parameters:
        - property_data (dict): Information about the property (size, slope, zoning compliance).
        - adu_designs (list): A list of possible ADU designs.

        Returns:
        - dict: Simulation results including best design, energy efficiency, and cost estimates.
        """

        print("\nStarting ADU Simulation...")

        # Validate Property Constraints
        property_model = PropertyModel(property_data)
        constraints = property_model.get_constraints()
        if not constraints["zoning_compliance"]:
            print("Property does not comply with zoning laws. Simulation terminated.")
            return {"error": "Property does not meet zoning requirements."}

        # GIS Analysis
        zoning_approved = self.gis_analyzer.analyze_zoning_constraints(property_data)
        if not zoning_approved:
            print("ADU placement is not permitted due to zoning restrictions.")
            return {"error": "Zoning constraints prevent ADU placement."}

        # Evaluate each ADU design
        design_results = []
        for design in adu_designs:
            efficiency = self.energy_model.compute_efficiency(design)
            energy_usage = self.energy_model.estimate_daily_energy_usage(design)
            total_cost = self.cost_estimator.estimate_total_cost(design)

            design_results.append({
                "design": design,
                "efficiency_score": efficiency,
                "daily_energy_usage": energy_usage,
                "total_cost": total_cost
            })

        # Find the best ADU design
        best_design = self.optimization_module.find_optimal_design(adu_designs)

        # Compile simulation results
        simulation_results = {
            "best_design": best_design,
            "all_designs": design_results,
            "zoning_approved": zoning_approved
        }

        print("\nSimulation Completed Successfully.")
        return simulation_results

# Example usage
if __name__ == "__main__":
    simulation_engine = SimulationEngine()

    # Sample property data
    property_data = {
        "size": 5000,
        "slope": 5,
        "zoning_compliance": True
    }

    # Sample ADU designs
    adu_designs = [
        {"floor_area": 600, "materials": "wood_frame", "hvac": "standard", "insulation": "standard"},
        {"floor_area": 750, "materials": "steel_frame", "hvac": "high_efficiency", "insulation": "high_efficiency"},
        {"floor_area": 900, "materials": "concrete", "hvac": "high_efficiency", "insulation": "passive_house"},
    ]

    # Run simulation
    results = simulation_engine.run_simulation(property_data, adu_designs)
    print("\nSimulation Results:")
    print(results)
