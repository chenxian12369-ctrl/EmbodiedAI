import torch

from torch.utils.data import (
    TensorDataset,
    DataLoader
)
x = torch.randn(
    100,
    20
)

target = torch.randn(
    100,
    6
)
dataset = TensorDataset(
    x,
    target
)
sample_x, sample_target = (
    dataset[0]
)

print(
    "sample x shape:",
    sample_x.shape
)

print(
    "sample target shape:",
    sample_target.shape
)
sample_x, sample_target = (
    dataset[0]
)

print(
    "sample x shape:",
    sample_x.shape
)

print(
    "sample target shape:",
    sample_target.shape
)

dataloader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)
for batch_x, batch_target in dataloader:

    print(
        "batch x:",
        batch_x.shape
    )

    print(
        "batch target:",
        batch_target.shape
    )

    break

for batch_index, (
    batch_x,
    batch_target
) in enumerate(dataloader):

    print(
        "batch:",
        batch_index,
        "shape:",
        batch_x.shape
    )
import torch.nn as nn


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

epochs = 3

for epoch in range(epochs):

    total_loss = 0.0

    for batch_x, batch_target in dataloader:

        optimizer.zero_grad()

        prediction = model(
            batch_x
        )

        loss = criterion(
            prediction,
            batch_target
        )

        loss.backward()

        optimizer.step()

        total_loss += (
            loss.item()
        )
        average_loss = (
    total_loss
    / len(dataloader)
)

    print(
        f"Epoch {epoch + 1}",
        f"average loss = {average_loss:.4f}"
    )

    print(
        f"Epoch {epoch + 1}",
        f"total loss = {total_loss:.4f}"
    )