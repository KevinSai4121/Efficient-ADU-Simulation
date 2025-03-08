from src.PropertyModel import PropertyModel
from src.ADUDesign import ADUDesign
from src.SimulationEngine import SimulationEngine
from src.EnergyModel import EnergyModel
from src.CostEstimator import CostEstimator
from src.GISAnalyzer import GISAnalyzer
from src.OptimizationModule import OptimizationModule

def main():
    print("Efficient ADU Design Simulation Starting...")

    # Sample Property Data
    property_data = {
        "size": 5000,  # Square feet
        "slope": 5,  # Degrees
        "zoning_compliance": True
    }

    # Sample ADU Design Data
    adu_design_data = {
        "floor_area": 600,  # Square feet
        "materials": "wood_frame",
        "hvac": "high_efficiency"
    }

    # Initialize Components
    property_model = PropertyModel(property_data)
    adu_design = ADUDesign(adu_design_data)
    simulation_engine = SimulationEngine()
    energy_model = EnergyModel()
    cost_estimator = CostEstimator()
    gis_analyzer = GISAnalyzer()
    optimization_module = OptimizationModule()

    # Validate Property Constraints
    print("\nChecking Property Constraints...")
    property_constraints = property_model.get_constraints()
    if not property_constraints["zoning_compliance"]:
        print("Property does not comply with zoning laws. Simulation terminated.")
        return
    print("Property meets zoning requirements.")

    # Generate ADU Design
    print("\nGenerating ADU Design...")
    livable_space = adu_design.calculate_livable_space()
    print(f"Livable Space: {livable_space} sq. ft.")

    # Run GIS Analysis
    print("\nRunning GIS Zoning Analysis...")
    zoning_approved = gis_analyzer.analyze_zoning_constraints(property_data)
    if not zoning_approved:
        print("ADU placement is not permitted due to zoning restrictions.")
        return
    print("Zoning Approved.")

    # Estimate Energy Efficiency
    print("\nCalculating Energy Efficiency...")
    energy_efficiency = energy_model.compute_efficiency(adu_design_data)
    print(f"Estimated Energy Efficiency: {energy_efficiency:.2f}")

    # Estimate Construction Cost
    print("\nEstimating Construction Cost...")
    total_cost = cost_estimator.estimate_total_cost(adu_design_data)
    print(f"Estimated Total Cost: ${total_cost:,.2f}")

    # Optimize ADU Configuration
    print("\nOptimizing ADU Configuration...")
    best_design = optimization_module.find_optimal_design([adu_design_data])
    print(f"Best ADU Design Selected: {best_design}")

    # Run Simulation
    print("\nRunning Full ADU Simulation...")
    simulation_results = simulation_engine.run_simulation()
    print("\nSimulation Results:")
    for key, value in simulation_results.items():
        print(f"   - {key}: {value}")

    print("\nEfficient ADU Simulation Completed Successfully.")

if __name__ == "__main__":
    main()
