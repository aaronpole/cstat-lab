import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
result = np.einsum('ij,jk->ik', A, B)

print("\nResult:")
print(result)