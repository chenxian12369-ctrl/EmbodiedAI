import torch

vector = torch.tensor(
    [10, 20, 30, 40]
)

print(
    vector[0]
)

print(
    vector[2]
)

matrix = torch.tensor(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

print(
    matrix[0]
)

print(
    matrix[1, 2]
)

vector = torch.tensor(
    [10, 20, 30, 40, 50]
)

print(
    vector[1:4]
)

matrix = torch.tensor(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

print(
    matrix[
        0:2,
        1:3
    ]
)

data = torch.tensor(
    [
        1, 2, 3,
        4, 5, 6
    ]
)

print(
    data.shape
)

matrix = data.reshape(
    2,
    3
)

print(
    matrix
)

print(
    matrix.shape
)
image = torch.zeros(
    3,
    224,
    224
)

print(
    image.shape
)
batch_image = image.unsqueeze(
    0
)

print(
    batch_image.shape
)
image_again = (
    batch_image.squeeze(0)
)

print(
    image_again.shape
)
output = torch.tensor(
    [
        [0.1, 0.7, 0.2]
    ]
)

print(
    output.shape
)

single_output = (
    output.squeeze(0)
)

print(
    single_output.shape
)