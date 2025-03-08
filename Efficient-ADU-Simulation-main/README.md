# Efficient-ADU-Simulation
For Modeling and Simulation Class

---

# **Efficient ADU Design Simulation**  
**CS 4632 - Modeling & Simulation**  
**Milestone 4 - Model Implementation**  
**Author:** Kevin Syhavong  

---

## **1. Project Overview**  
The **Efficient ADU Design Simulation** models the **design, placement, and feasibility** of **Accessory Dwelling Units (ADUs)** on existing residential properties. The simulation integrates:  

-  **Zoning regulations** (property constraints, slopes)  
-  **Energy efficiency modeling** (HVAC, solar exposure)  
-  **Construction cost estimation**  
-  **Geospatial analysis** (GIS-based zoning compliance)  
-  **Optimization module** to refine ADU design choices  

### **Objectives:**  
- Simulate **ADU placement feasibility** based on property constraints  
- Model **energy efficiency** using OpenStudio/EnergyPlus  
- Estimate **construction costs** for different ADU designs  
- Optimize ADU configurations for **maximum livability**  

---

## **2️. Implementation Status**  
### **Current Progress (Milestone 4):**  
-  **Implemented foundational classes** (`PropertyModel`, `ADUDesign`, `SimulationEngine`, etc.)  
-  **Basic simulation engine structure built**  
-  **Energy model partially integrated** (initial framework for HVAC and solar exposure)  
-  **Test cases drafted for validation**  

### **Next Steps (For Future Milestones):**  
-  **Enhance energy modeling integration**  
-  **Improve cost estimator accuracy**  
-  **Add GIS-based zoning compliance module**  
-  **Implement ADU optimization strategies**  

---

## **3️. Repository Structure**  
 **GitHub Repository:** [Insert Link Here]  

```
 Efficient_ADU_Simulation_CS4632
 ┣  src/              # Core simulation code  
 ┣  docs/             # UML diagrams, literature review, and reports  
 ┣  tests/            # Planned test cases and validation scripts  
 ┣  README.md        # Project description and setup guide  
 ┗  requirements.txt  # Dependencies for execution  
```

---

## **4️. Setup & Installation Instructions**  
### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Efficient_ADU_Simulation_CS4632.git
cd Efficient_ADU_Simulation_CS4632
```

### **Step 2: Set Up Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 4: Run the Simulation**  
```bash
python src/simulation.py
```

---

## **5️. Project Components & Code Explanation**  
### **PropertyModel**
Handles **zoning laws, slope constraints, and available space**.  
 **Methods:** `get_constraints()`, `check_feasibility()`

### **ADUDesign**
Generates **floor plans, material selection, and efficiency metrics**.  
 **Methods:** `generate_design()`, `calculate_livable_space()`

### **SimulationEngine**
Executes **various ADU design scenarios** and collects results.  
 **Methods:** `run_simulation()`, `collect_data()`

### **EnergyModel**
Computes **energy efficiency based on ADU design choices**.  
 **Methods:** `compute_efficiency()`, `analyze_energy_usage()`

### **CostEstimator**
Evaluates **total construction costs** using material pricing and labor expenses.  
 **Methods:** `estimate_total_cost()`

### **GISAnalyzer**
Uses **geospatial data** to assess zoning constraints.  
 **Methods:** `analyze_zoning_constraints()`, `evaluate_sunlight_exposure()`

### **OptimizationModule**
Identifies **optimal ADU configurations** based on multiple factors.  
 **Methods:** `find_optimal_design()`, `suggest_improvements()`

---

## **6️. Test Plan & Validation**  
### **Planned Test Cases:**  
-  Verify **ADU placement feasibility** using sample properties  
-  Validate **energy efficiency calculations** against known benchmarks  
-  Confirm **cost estimations** align with industry standards  

### **Testing Frameworks:**  
-  **Unit tests using `pytest`**  
-  **Performance testing for simulation run-time**  

---

## **7️. UML Diagram & Documentation Updates**  
 UML Diagram Location: `docs/CS_4632_W01_KevinSyhavong_Milestone4_UML.pdf`  

-  **Updated UML reflects new method implementations**  
-  **Documentation includes literature review alignment**  

---

## **8️. Future Enhancements**  
-  **Enhance optimization strategies for cost vs. energy trade-offs**  
-  **Improve simulation visualization (graphs, heatmaps)**  
-  **Expand validation against real-world ADU datasets**  

---

## **9️. References & Sources**  
1️. DOE OpenStudio Documentation  
2️. GIS-based Zoning Analysis for ADU Placement  
3️. Discrete-Event Simulation for Urban Planning  
4️. EnergyPlus Building Energy Modeling  

---
