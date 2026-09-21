import torch
import torch.nn as nn

layer = nn.Linear(
    in_features=20,
    out_features=6
)

print(layer)
x = torch.randn(
    64,
    20
)

output = layer(x)

print(
    "input shape:",
    x.shape
)

print(
    "output shape:",
    output.shape
)

print(
    "weight shape:",
    layer.weight.shape
)

print(
    "bias shape:",
    layer.bias.shape
)
class SimpleNetwork(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc = nn.Linear(
            20,
            6
        )

    def forward(
        self,
        x
    ):

        output = self.fc(x)

        return output

model = SimpleNetwork()

x = torch.randn(
    64,
    20
)

output = model(x)

print(
    "model output shape:",
    output.shape
)
for name, parameter in model.named_parameters():

    print(
        name,
        parameter.shape
    )