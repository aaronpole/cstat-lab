import numpy as np

arr = np.array([1, 4, 9, 16, 25, 36])
n = int(input("Enter the order: "))

result = np.diff(arr, n)

print("Nth Order Difference:")
print(result)