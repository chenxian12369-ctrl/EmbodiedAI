import torch
a = torch.tensor(
    [1.0, 2.0, 3.0]
)

b = 10.0

print(
    a + b
)

x = torch.randn(
    32,
    10
)

weight = torch.randn(
    10,
    5
)

bias = torch.randn(
    5
)

output = (
    x @ weight
    + bias
)

print(
    "x shape:",
    x.shape
)

print(
    "weight shape:",
    weight.shape
)

print(
    "bias shape:",
    bias.shape
)

print(
    "output shape:",
    output.shape
)