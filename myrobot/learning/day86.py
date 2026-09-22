import torch
import torch.nn as nn

prediction = torch.tensor(
    [2.0, 4.0]
)

target = torch.tensor(
    [1.0, 5.0]
)

criterion = nn.MSELoss()

loss = criterion(
    prediction,
    target
)

print(
    "prediction:",
    prediction
)

print(
    "target:",
    target
)

print(
    "loss:",
    loss
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

x = torch.randn(
    64,
    20
)

target = torch.randn(
    64,
    6
)

prediction = model(x)

criterion = nn.MSELoss()

loss = criterion(
    prediction,
    target
)

print(
    "prediction shape:",
    prediction.shape
)

print(
    "target shape:",
    target.shape
)

print(
    "loss:",
    loss
)

prediction_good = torch.tensor(
    [1.1, 4.9]
)

prediction_bad = torch.tensor(
    [3.0, 8.0]
)

target = torch.tensor(
    [1.0, 5.0]
)

good_loss = criterion(
    prediction_good,
    target
)

bad_loss = criterion(
    prediction_bad,
    target
)

print(
    "good loss:",
    good_loss
)

print(
    "bad loss:",
    bad_loss
)