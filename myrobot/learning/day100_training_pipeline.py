import os

import torch
import torch.nn as nn

from torch.utils.data import DataLoader
from torchvision import datasets, transforms
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(
    "device:",
    device
)
transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform
)

validation_dataset = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=128,
    shuffle=True
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=128,
    shuffle=False
)
class MNISTCNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.conv1 = nn.Conv2d(
            1,
            8,
            kernel_size=3,
            padding=1
        )

        self.relu1 = nn.ReLU()

        self.pool1 = nn.MaxPool2d(
            2,
            2
        )

        self.conv2 = nn.Conv2d(
            8,
            16,
            kernel_size=3,
            padding=1
        )

        self.relu2 = nn.ReLU()

        self.pool2 = nn.MaxPool2d(
            2,
            2
        )

        self.flatten = nn.Flatten()

        self.dropout = nn.Dropout(
            p=0.5
        )

        self.fc = nn.Linear(
            16 * 7 * 7,
            10
        )

    def forward(
        self,
        x
    ):

        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)

        x = self.flatten(x)
        x = self.dropout(x)

        x = self.fc(x)

        return x
model = MNISTCNN().to(device)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
def train_one_epoch(
    model,
    loader,
    criterion,
    optimizer,
    device
):

    model.train()

    total_loss = 0.0
    correct = 0
    total = 0

    for batch_x, batch_target in loader:

        batch_x = batch_x.to(device)
        batch_target = batch_target.to(device)

        optimizer.zero_grad()

        logits = model(
            batch_x
        )

        loss = criterion(
            logits,
            batch_target
        )

        loss.backward()

        optimizer.step()

        predicted_classes = torch.argmax(
            logits,
            dim=1
        )

        correct += (
            predicted_classes
            == batch_target
        ).sum().item()

        total += batch_target.size(0)

        total_loss += (
            loss.item()
            * batch_x.size(0)
        )

    average_loss = (
        total_loss
        / total
    )

    accuracy = (
        correct
        / total
    )

    return (
        average_loss,
        accuracy
    )
def evaluate(
    model,
    loader,
    criterion,
    device
):

    model.eval()

    total_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():

        for batch_x, batch_target in loader:

            batch_x = batch_x.to(device)
            batch_target = batch_target.to(device)

            logits = model(
                batch_x
            )

            loss = criterion(
                logits,
                batch_target
            )

            predicted_classes = torch.argmax(
                logits,
                dim=1
            )

            correct += (
                predicted_classes
                == batch_target
            ).sum().item()

            total += batch_target.size(0)

            total_loss += (
                loss.item()
                * batch_x.size(0)
            )

    average_loss = (
        total_loss
        / total
    )

    accuracy = (
        correct
        / total
    )

    return (
        average_loss,
        accuracy
    )
os.makedirs(
    "models",
    exist_ok=True
)
best_validation_accuracy = 0.0

best_model_path = (
    "models/day100_best_mnist_cnn.pth"
)
epochs = 5

for epoch in range(epochs):

    train_loss, train_accuracy = (
        train_one_epoch(
            model,
            train_loader,
            criterion,
            optimizer,
            device
        )
    )

    validation_loss, validation_accuracy = (
        evaluate(
            model,
            validation_loader,
            criterion,
            device
        )
    )

    print(
        f"Epoch {epoch + 1}",
        f"train loss={train_loss:.4f}",
        f"train acc={train_accuracy:.4f}",
        f"val loss={validation_loss:.4f}",
        f"val acc={validation_accuracy:.4f}"
    )
    if (
        validation_accuracy
        > best_validation_accuracy
    ):

        best_validation_accuracy = (
            validation_accuracy
        )

        torch.save(
            model.state_dict(),
            best_model_path
        )

        print(
            "保存新的 best model:",
            best_validation_accuracy
        )
print(
    "training finished"
)
best_model = MNISTCNN().to(device)
state_dict = torch.load(
    best_model_path,
    map_location=device
)

best_model.load_state_dict(
    state_dict
)

best_model.eval()
best_loss, best_accuracy = (
    evaluate(
        best_model,
        validation_loader,
        criterion,
        device
    )
)

print(
    "best model accuracy:",
    best_accuracy
)