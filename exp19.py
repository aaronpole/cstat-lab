import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[0, 5],
              [6, 7]])


result = np.kron(A, B)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nKronecker Product:")
print(result)