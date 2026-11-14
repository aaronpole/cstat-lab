import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
print("3D Array:")
print(arr)
print("\n2D Diagonals:")
for i in range(arr.shape[0]):
    print(np.diagonal(arr[i]))