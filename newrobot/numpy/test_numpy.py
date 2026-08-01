# import numpy as np

# print("NumPy版本：", np.__version__)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a)
# print(b)

# print(a + b)
# print(a * b)



# a = np.array([
#     [1,2],
#     [3,4]
# ])

# print(a[0])
# print(a[1])
# print(a[0][1])

# import numpy as np

# a = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(a[1])

# print(a[:,1])

# print(a[:2,:2])

# print(a[:,-1])

# print(a[2])

# print(a[0:2])

# print(a[1:,1:])

# a = np.array([3,5])

# b = np.array([2,1])

# print(a+b)

# print(a-b)

# print(a*2)

# print(a/2)
# print([3,5]+[2,1])day30



# day31a = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(a)
# print(a + 10)
# print(a * 2)
# b = np.array([10,20,30])

# print(a+b)
# print(a-1)

# print(a/2)
import numpy as np

# A = np.array([
#     [1,2],
#     [3,4]
# ])

# B = np.array([
#     [5],
#     [6]
# ])
# print(A@B)
# print(A*2)
# print(A@A)



# a = np.array([1,0])

# b = np.array([1,0])

# c = np.array([0,1])

# d = np.array([-1,0])


# print(a @ b)

# print(a @ c)

# print(a @ d)
# move = np.array([3,4])
# length = np.linalg.norm(move)

# print(length)

# point = np.array([
#     1,
#     0
# ])


# R = np.array([
#     [0,-1],
#     [1,0]
# ])


# new_point = R @ point


# print(new_point)
# point = np.array([
#     1,
#     2,
#     1
# ])


# T = np.array([
#     [1,0,10],
#     [0,1,5],
#     [0,0,1]
# ])


# new_point = T @ point


# print(new_point)

# point=np.array([
#     1,
#     0
# ])


# R=np.array([
#     [0,-1],
#     [1,0]
# ])


# print(R @ point)
# R=np.array([
#     [-1,0],
#     [0,-1]
# ])
# print(R @ point)
import numpy as np


T=np.array([
    [1,0,10],
    [0,1,5],
    [0,0,1]
])


p=np.array([
    2,
    3,
    1
])


print(T@p)

T1=np.array([
    [1,0,10],
    [0,1,0],
    [0,0,1]
])

T2=np.array([
    [1,0,0],
    [0,1,5],
    [0,0,1]
])

point=np.array([
    1,
    1,
    1
])

print(T@point)


# 平移
T=np.array([
    [1,0,10],
    [0,1,0],
    [0,0,1]
])


# 旋转90度
R=np.array([
    [0,-1,0],
    [1,0,0],
    [0,0,1]
])


point=np.array([
    1,
    0,
    1
])


print("先平移再旋转")
print(R@T@point)


print("先旋转再平移")
print(T@R@point)

T_robot_camera = np.array([
    [1,0,2],
    [0,1,0],
    [0,0,1]
])
T_world_robot = np.array([
    [1,0,10],
    [0,1,0],
    [0,0,1]
])
T_world_camera = T_world_robot @ T_robot_camera
print(T_world_camera)