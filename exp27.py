import numpy as np
import matplotlib.pyplot as plt

arr = np.array([10, 25, 15, 30, 20, 35])

plt.plot(arr, marker='o')
plt.title("Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()
plt.show()