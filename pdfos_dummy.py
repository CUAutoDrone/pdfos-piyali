import numpy as np
from pdfo import pdfo

# Objective Function (non-linear)
def objective(params):
    x, y = params
    return (x - 3)**4 + (2 - y)**2

# Linear Constraints
def constraint1(params):
    x, y = params
    return 10 - (x + y)  # >= 0

def constraint2(params):
    x, y = params
    return y - x + 15  # >= 0

# Defining bounds for variables (x, y)
bounds = [(0, 5),  # x bounds
          (0, 5)]  # y bounds

# Initial guess for x and y
x0 = [0, 0]  # Starting point for optimization

# Constraints for PDFO
constraints_list = [
    {'type': 'ineq', 'fun': constraint1},  # x + y <= 10
    {'type': 'ineq', 'fun': constraint2}   # x - y >= 15
]

# Running PDFO optimization
# Minimizes by default
def run_pdfo_optimization():
    # Running PDFO with bounds, constraints, and initial guess
    result = pdfo(objective, x0=x0, bounds=bounds, constraints=constraints_list)
    
    # Displaying the result
    print(f"Optimal parameters: {result.x}")
    print(f"Optimal objective value: {result.fun}")
    return result


# Execute the optimization
if __name__ == "__main__":
    run_pdfo_optimization()