from src.SimulationEngine import SimulationEngine
import matplotlib.pyplot as plt

def main():
    print("Efficient ADU Design Simulation Starting...\n")

    # Property Data (valid for zoning in Cartersville)
    property_data = {
        "size": 5000,
        "slope": 5,
        "zoning_compliance": True
    }

    # List of 5 different ADU designs
    adu_designs = [
        {"floor_area": 600, "materials": "wood_frame", "hvac": "standard", "insulation": "standard"},
        {"floor_area": 700, "materials": "steel_frame", "hvac": "high_efficiency", "insulation": "high_efficiency"},
        {"floor_area": 800, "materials": "concrete", "hvac": "high_efficiency", "insulation": "passive_house"},
        {"floor_area": 750, "materials": "wood_frame", "hvac": "high_efficiency", "insulation": "high_efficiency"},
        {"floor_area": 1000, "materials": "concrete", "hvac": "high_efficiency", "insulation": "high_efficiency"},
    ]

    # Initialize Simulation Engine
    simulation_engine = SimulationEngine()

    # Run full simulation with all designs
    results = simulation_engine.run_simulation(property_data, adu_designs)

    print("\n===== Simulation Results =====")
    if "error" in results:
        print(f"Simulation Error: {results['error']}")
        return

    print(f"\nBest Design Selected: {results['best_design']}")

    print("\nAll Design Results:")
    for i, res in enumerate(results["all_designs"], start=1):
        floor_area = res["design"]["floor_area"]

        # Calculate additional normalized metrics
        res["energy_per_sqft"] = round(res["daily_energy_usage"] / floor_area, 4)
        res["cost_per_sqft"] = round(res["total_cost"] / floor_area, 2)

        # Print results
        print(f"\n--- Design {i} ---")
        print(f"Design: {res['design']}")
        print(f"Efficiency Score: {res['efficiency_score']}")
        print(f"Daily Energy Usage: {res['daily_energy_usage']} kWh")
        print(f"Total Cost: ${res['total_cost']:,.2f}")
        print(f"Energy Usage per Sq Ft: {res['energy_per_sqft']} kWh/sq ft")
        print(f"Cost per Sq Ft: ${res['cost_per_sqft']}")

    # 📊 Auto-generate updated graphs
    floor_areas = [res["design"]["floor_area"] for res in results["all_designs"]]
    costs = [res["total_cost"] for res in results["all_designs"]]
    efficiencies = [res["efficiency_score"] for res in results["all_designs"]]
    energy_usages = [res["daily_energy_usage"] for res in results["all_designs"]]
    energy_per_sqft = [res["energy_per_sqft"] for res in results["all_designs"]]
    cost_per_sqft = [res["cost_per_sqft"] for res in results["all_designs"]]

    # 1. Bar Chart - Floor Area vs. Total Cost
    plt.figure()
    plt.bar([str(fa) + " sq ft" for fa in floor_areas], costs)
    plt.title("Floor Area vs. Total Cost")
    plt.xlabel("ADU Floor Area (sq ft)")
    plt.ylabel("Cost (USD)")
    plt.tight_layout()
    plt.savefig("floor_area_vs_cost.png")

    # 2. Line Chart - Floor Area vs. Energy Efficiency
    plt.figure()
    plt.plot(floor_areas, efficiencies, marker='o')
    plt.title("Floor Area vs. Energy Efficiency")
    plt.xlabel("ADU Floor Area (sq ft)")
    plt.ylabel("Efficiency Score")
    plt.tight_layout()
    plt.savefig("floor_area_vs_efficiency.png")

    # 3. Scatter Plot - Total Cost vs. Efficiency
    plt.figure()
    plt.scatter(costs, efficiencies)
    plt.title("Total Cost vs. Energy Efficiency")
    plt.xlabel("Total Cost (USD)")
    plt.ylabel("Efficiency Score")
    plt.tight_layout()
    plt.savefig("cost_vs_efficiency.png")

    # 4. Line Chart - Floor Area vs. Energy Use per Sq Ft
    plt.figure()
    plt.plot(floor_areas, energy_per_sqft, marker='o', color='green')
    plt.title("Floor Area vs. Energy Use per Sq Ft")
    plt.xlabel("ADU Floor Area (sq ft)")
    plt.ylabel("Energy Use (kWh/sq ft)")
    plt.tight_layout()
    plt.savefig("floor_area_vs_energy_per_sqft.png")

    # 5. Line Chart - Floor Area vs. Cost per Sq Ft
    plt.figure()
    plt.plot(floor_areas, cost_per_sqft, marker='o', color='red')
    plt.title("Floor Area vs. Cost per Sq Ft")
    plt.xlabel("ADU Floor Area (sq ft)")
    plt.ylabel("Cost per Sq Ft (USD)")
    plt.tight_layout()
    plt.savefig("floor_area_vs_cost_per_sqft.png")

    print("\n✅ Graphs updated and saved as PNG files.")

    print("\nEfficient ADU Simulation Completed Successfully.")

if __name__ == "__main__":
    main()
