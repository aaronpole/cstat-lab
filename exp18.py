import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

inner = np.inner(a, b)
outer = np.outer(a, b)
cross = np.cross(a, b)

print("Vector a:")
print(a)
print("\nVector b:")
print(b)

print("Inner Product:")
print(inner)

print("\nOuter Product:")
print(outer)

print("\nCross Product:")
print(cross)