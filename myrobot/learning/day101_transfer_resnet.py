import torch
import torch.nn as nn

from torchvision.models import (
    resnet18,
    ResNet18_Weights
)


device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(
    "device:",
    device
)


weights = ResNet18_Weights.DEFAULT


model = resnet18(
    weights=weights
)


print(
    "original fc:",
    model.fc
)


for parameter in model.parameters():

    parameter.requires_grad = False


input_features = (
    model.fc.in_features
)


model.fc = nn.Linear(
    input_features,
    3
)


print(
    "new fc:",
    model.fc
)


print(
    "\nTrainable parameters:"
)


for name, parameter in model.named_parameters():

    if parameter.requires_grad:

        print(
            name,
            parameter.shape
        )


optimizer = torch.optim.Adam(
    filter(
        lambda parameter:
            parameter.requires_grad,
        model.parameters()
    ),
    lr=0.001
)


model = model.to(device)


images = torch.randn(
    8,
    3,
    224,
    224
).to(device)


logits = model(
    images
)


print(
    "input shape:",
    images.shape
)

print(
    "logits shape:",
    logits.shape
)