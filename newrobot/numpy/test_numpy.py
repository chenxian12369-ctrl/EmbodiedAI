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

import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a[1])

print(a[:,1])

print(a[:2,:2])

print(a[:,-1])

print(a[2])

print(a[0:2])

print(a[1:,1:])

a = np.array([3,5])

b = np.array([2,1])

print(a+b)

print(a-b)

print(a*2)

print(a/2)
print([3,5]+[2,1])