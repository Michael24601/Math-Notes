import numpy as np

# Define the matrix
A = np.array([[1, 1, 0],
              [0, 1, 5],
              [1, 1, 1]])

# Define the vector
v = np.array([13, -10, 3])

# Multiply
result = A @ v

print("Result:\n", result)
