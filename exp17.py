import numpy as np

A = np.array([[4, 7],
              [2, 6]])

print("Matrix:")
print(A)

inverse = np.linalg.inv(A)

print("\nInverse:")
print(inverse)