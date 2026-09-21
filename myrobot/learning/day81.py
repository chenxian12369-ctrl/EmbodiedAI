import torch


number = torch.tensor(5)

print(number)
print(number.shape)

vector = torch.tensor(
    [1, 2, 3]
)

print(vector)
print(vector.shape)

matrix = torch.tensor(
    [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
)

print(matrix)
print(matrix.shape)

image = torch.zeros(
    3,
    480,
    640
)

print(
    "image shape:",
    image.shape
)

batch = torch.zeros(
    8,
    3,
    480,
    640
)

print(
    "batch shape:",
    batch.shape
)

data = torch.tensor(
    [1.0, 2.0, 3.0]
)

print(
    "dtype:",
    data.dtype
)

a = torch.tensor(
    [1.0, 2.0, 3.0]
)

b = torch.tensor(
    [4.0, 5.0, 6.0]
)

print(
    "a + b =",
    a + b
)

print(
    "a * b =",
    a * b
)