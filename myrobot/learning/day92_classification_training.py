import torch
import torch.nn as nn

from torch.utils.data import (
    TensorDataset,
    DataLoader,
    random_split
)

sample_count = 1000

x = torch.randn(
    sample_count,
    2
)

target = (
    x[:, 0]
    + x[:, 1]
    > 0
).long()

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
class ClassificationNetwork(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc1 = nn.Linear(
            2,
            16
        )

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(
            16,
            2
        )

    def forward(
        self,
        x
    ):

        x = self.fc1(x)

        x = self.relu(x)

        x = self.fc2(x)

        return x
model = ClassificationNetwork()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.1
)
epochs = 10


for epoch in range(epochs):

    # =========================
    # 1. 训练阶段
    # =========================

    model.train()

    total_train_loss = 0.0
    train_correct = 0
    train_total = 0

    for batch_x, batch_target in train_loader:

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

        correct = (
            predicted_classes
            == batch_target
        )

        train_correct += (
            correct.sum().item()
        )

        train_total += (
            batch_target.size(0)
        )

        total_train_loss += (
            loss.item()
            * batch_x.size(0)
        )

    # 🔴【修改】
    # 整个训练集跑完以后再计算
    average_train_loss = (
        total_train_loss
        / len(train_dataset)
    )

    train_accuracy = (
        train_correct
        / train_total
    )

    # =========================
    # 2. 验证阶段
    # =========================

    # 🔴【新增】
    model.eval()

    # 🔴【新增】
    total_validation_loss = 0.0

    # 🔴【新增】
    validation_correct = 0

    # 🔴【新增】
    validation_total = 0

    with torch.no_grad():

        for batch_x, batch_target in validation_loader:

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

            correct = (
                predicted_classes
                == batch_target
            )

            validation_correct += (
                correct.sum().item()
            )

            validation_total += (
                batch_target.size(0)
            )

            total_validation_loss += (
                loss.item()
                * batch_x.size(0)
            )

    average_validation_loss = (
        total_validation_loss
        / len(validation_dataset)
    )

    validation_accuracy = (
        validation_correct
        / validation_total
    )

    # =========================
    # 3. 打印本轮结果
    # =========================


    print(
        f"Epoch {epoch + 1}",
        f"train loss={average_train_loss:.4f}",
        f"train acc={train_accuracy:.4f}",
        f"val loss={average_validation_loss:.4f}",
        f"val acc={validation_accuracy:.4f}"
    )