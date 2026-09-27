import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

Q, R = np.linalg.qr(A)

print("Matrix A:")
print(A)

print("\nMatrix Q:")
print(Q)

print("\nMatrix R:")
print(R)