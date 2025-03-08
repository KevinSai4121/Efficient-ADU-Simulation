import pytest
from src.PropertyModel import PropertyModel
from src.ADUDesign import ADUDesign
from src.SimulationEngine import SimulationEngine
from src.EnergyModel import EnergyModel
from src.CostEstimator import CostEstimator
from src.GISAnalyzer import GISAnalyzer
from src.OptimizationModule import OptimizationModule

# Sample data for testing
property_data = {
    "size": 5000,  # Square feet
    "slope": 5,  # Degrees
    "zoning_compliance": True
}

adu_design_data = {
    "floor_area": 600,  # Square feet
    "materials": "wood_frame",
    "hvac": "high_efficiency"
}

@pytest.fixture
def property_model():
    return PropertyModel(property_data)

@pytest.fixture
def adu_design():
    return ADUDesign(adu_design_data)

@pytest.fixture
def simulation_engine():
    return SimulationEngine()

@pytest.fixture
def energy_model():
    return EnergyModel()

@pytest.fixture
def cost_estimator():
    return CostEstimator()

@pytest.fixture
def gis_analyzer():
    return GISAnalyzer()

@pytest.fixture
def optimization_module():
    return OptimizationModule()

# Test Case 1: Property Model Validation
def test_property_constraints(property_model):
    constraints = property_model.get_constraints()
    assert constraints["size"] > 0, "Property size should be positive"
    assert 0 <= constraints["slope"] <= 45, "Slope should be between 0 and 45 degrees"
    assert isinstance(constraints["zoning_compliance"], bool), "Zoning compliance should be a boolean"

# Test Case 2: ADU Design Calculation
def test_adu_design(adu_design):
    livable_space = adu_design.calculate_livable_space()
    assert livable_space > 0, "Livable space should be greater than zero"
    
# Test Case 3: Energy Efficiency Calculation
def test_energy_model(energy_model):
    efficiency = energy_model.compute_efficiency(adu_design_data)
    assert 0 <= efficiency <= 1, "Energy efficiency should be between 0 and 1"

# Test Case 4: Cost Estimation
def test_cost_estimator(cost_estimator):
    cost = cost_estimator.estimate_total_cost(adu_design_data)
    assert cost > 0, "Total cost should be positive"

# Test Case 5: GIS Analysis
def test_gis_analyzer(gis_analyzer):
    zoning_passed = gis_analyzer.analyze_zoning_constraints(property_data)
    assert isinstance(zoning_passed, bool), "Zoning analysis should return a boolean"

# Test Case 6: Optimization Module
def test_optimization_module(optimization_module):
    best_design = optimization_module.find_optimal_design([adu_design_data])
    assert best_design is not None, "Optimization should return a valid design"

# Test Case 7: Simulation Execution
def test_simulation_execution(simulation_engine):
    result = simulation_engine.run_simulation()
    assert isinstance(result, dict), "Simulation should return a dictionary of results"
    assert "energy_usage" in result, "Simulation results should include energy usage"
    assert "total_cost" in result, "Simulation results should include total cost"
