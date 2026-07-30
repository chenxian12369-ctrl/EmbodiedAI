import numpy as np

print("NumPy版本：", np.__version__)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a)
print(b)

print(a + b)
print(a * b)



a = np.array([
    [1,2],
    [3,4]
])

print(a[0])
print(a[1])
print(a[0][1])