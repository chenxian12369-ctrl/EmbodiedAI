import torch
import torch.nn as nn

from torch.utils.data import (
    TensorDataset,
    DataLoader,
    random_split
)
x = torch.randn(
    1000,
    20
)

target = torch.randn(
    1000,
    6
)

dataset = TensorDataset(
    x,
    target
)

train_size = 800

validation_size = 200

train_dataset, validation_dataset = (
    random_split(
        dataset,
        [
            train_size,
            validation_size
        ]
    )
)

print(
    "train size:",
    len(train_dataset)
)

print(
    "validation size:",
    len(validation_dataset)
)

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=32,
    shuffle=False
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

epochs = 5


for epoch in range(epochs):

    model.train()

    train_loss = 0.0

    for batch_x, batch_target in train_loader:

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

        train_loss += (
            loss.item()
            * batch_x.size(0)
        )

    average_train_loss = (
        train_loss
        / len(train_dataset)
    )

model.eval()

validation_loss = 0.0

with torch.no_grad():

        for batch_x, batch_target in validation_loader:

            prediction = model(
                batch_x
            )

            loss = criterion(
                prediction,
                batch_target
            )

            validation_loss += (
                loss.item()
                * batch_x.size(0)
            )
average_validation_loss = (
        validation_loss
        / len(validation_dataset)
    )
print(
        f"Epoch {epoch + 1}",
        f"train loss = {average_train_loss:.4f}",
        f"validation loss = {average_validation_loss:.4f}"
    )
model.train()

for batch_x, batch_target in train_loader:

    optimizer.zero_grad()

    prediction = model(batch_x)

    loss = criterion(
        prediction,
        batch_target
    )

    loss.backward()

    optimizer.step()
model.eval()

with torch.no_grad():

    for batch_x, batch_target in validation_loader:

        prediction = model(batch_x)

        loss = criterion(
            prediction,
            batch_target
        )