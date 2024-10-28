import numpy as np
from pdfo import pdfo
import time

# Objective Function (non-linear)
def objective(params):
    x, y = params
    return (x - 3)**4 + (2 - y)**8 + (y**0.00002 * x**200)

# Wrapper for logging with timing
class Logger:
    def __init__(self):
        self.last_print_time = time.time()  # Initialize with the current time

    def logging_objective(self, params):
        current_time = time.time()
        value = objective(params)

        # Check if 1 second has passed since the last print
        if current_time - self.last_print_time >= 0.1:
            print(f"Evaluating at params: {params}, Objective value: {value}")
            self.last_print_time = current_time  # Update the last print time
        
        return value

# Create a logger instance
logger = Logger()

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
def run_pdfo_optimization():
    # Running PDFO with bounds, constraints, and initial guess
    result = pdfo(logger.logging_objective, x0=x0, bounds=bounds, constraints=constraints_list)
    
    # Displaying the result
    print(f"Optimal parameters: {result.x}")
    print(f"Optimal objective value: {result.fun}")
    return result

# Execute the optimization
if __name__ == "__main__":
    run_pdfo_optimization()
