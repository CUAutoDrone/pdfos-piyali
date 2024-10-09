import numpy as np
from pdfo import pdfo

# Constants
Vin = 100  # Initial velocity (m/s), example value
rpm = 40000  # RPM (rotations per minute), constant
yield_stress = 500  # Yield stress for carbon fiber, example value

# Thrust efficiency function (to be defined properly)
def thrust_efficiency(prop_diameter, pitch, height, temp):
    # Placeholder function; modify based on actual aerodynamic equations
    return (prop_diameter * pitch) / (height + temp + 1)  # Simplified example

# Strain penalty function (exponentially increasing near the yield stress)
def strain_penalty(strain):
    if strain > yield_stress:
        return np.exp(strain - yield_stress)  # Exponential penalty for exceeding yield stress
    return 0  # No penalty if within limits

# Objective function for optimization
def objective(params):
    prop_diameter, pitch, height, temp = params
    efficiency = thrust_efficiency(prop_diameter, pitch, height, temp)
    strain = (prop_diameter * pitch) / (height + temp + 1)  # Simplified strain formula
    penalty = strain_penalty(strain)
    return -1 * (efficiency - penalty)  # Negative because we are minimizing in optimizers

# Constraint: strain should not exceed yield stress
def strain_constraint(params):
    prop_diameter, pitch, height, temp = params
    strain = (prop_diameter * pitch) / (height + temp + 1)  # Simplified strain formula
    return yield_stress - strain  # Positive if strain < yield stress, as required by PDFO

# Bounds for parameters (propeller diameter, pitch, height, temperature)
bounds = [(0.1, 1.0),  # Propeller diameter (meters)
          (0.1, 1.0),  # Pitch (meters)
          (0, 10000),  # Height (meters)
          (-50, 50)]   # Temperature (Celsius)

# Constraints for PDFO
constraints_list = [{'type': 'ineq', 'fun': strain_constraint}, {prop_diameter > 0}]

# Running PDFO optimization
def run_pdfo_optimization():
    # Running PDFO with bounds and constraints
    result = pdfo(objective, bounds=bounds, constraints=constraints_list)
    
    # Displaying the result
    print(f"Optimal parameters: {result.x}")
    print(f"Optimal objective value (negative thrust efficiency minus penalty): {result.fun}")
    return result

# Execute the optimization
if __name__ == "__main__":
    run_pdfo_optimization()
