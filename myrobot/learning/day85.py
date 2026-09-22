import torch
import torch.nn as nn
relu = nn.ReLU()

x = torch.tensor(
    [
        -5.0,
        -2.0,
        0.0,
        3.0,
        8.0
    ]
)

output = relu(x)

print(
    "ReLU input:",
    x
)

print(
    "ReLU output:",
    output
)

class SimpleNetwork(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc1 = nn.Linear(
            20,
            32
        )

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(
            32,
            6
        )

    def forward(
    self,
    x
):

        print(
            "进入网络：",
            x.shape
        )

        x = self.fc1(x)

        print(
            "fc1之后：",
            x.shape
        )

        x = self.relu(x)

        print(
            "ReLU之后：",
            x.shape
        )

        x = self.fc2(x)

        print(
            "fc2之后：",
            x.shape
        )

        return x
model = SimpleNetwork()

x = torch.randn(
    64,
    20
)

output = model(x)

print(
    "input shape:",
    x.shape
)

print(
    "output shape:",
    output.shape
)

print(model)
total_parameters = sum(
    parameter.numel()
    for parameter
    in model.parameters()
)

print(
    "总参数数量：",
    total_parameters
)