import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

np.savetxt("array.csv", arr, delimiter=",", fmt="%d")

print("NumPy array successfully converted to array.csv")