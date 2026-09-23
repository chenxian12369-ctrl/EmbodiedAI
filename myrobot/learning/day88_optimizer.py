import torch
import torch.nn as nn

weight = torch.tensor(
    2.0,
    requires_grad=True
)

x = torch.tensor(
    3.0
)

target = torch.tensor(
    10.0
)

learning_rate = 0.01

optimizer = torch.optim.SGD(
    [weight],
    lr=0.01
)

for step in range(10):

    prediction = (
        weight * x
    )

    loss = (
        prediction - target
    ) ** 2

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print(
        f"step={step}",
        f"weight={weight.item():.4f}",
        f"prediction={prediction.item():.4f}",
        f"loss={loss.item():.4f}",
        f"grad={weight.grad.item():.4f}"
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

        x = self.fc1(x)

        x = self.relu(x)

        x = self.fc2(x)

        return x
model = SimpleNetwork()

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

x = torch.randn(
    64,
    20
)

target = torch.randn(
    64,
    6
)

for step in range(10):

    optimizer.zero_grad()

    prediction = model(x)

    loss = criterion(
        prediction,
        target
    )

    loss.backward()

    optimizer.step()

    print(
        f"step={step}",
        f"loss={loss.item():.4f}"
    )