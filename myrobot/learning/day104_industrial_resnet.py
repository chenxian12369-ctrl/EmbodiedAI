import os

import torch
import torch.nn as nn

from torch.utils.data import DataLoader

from torchvision import (
    datasets,
    transforms
)

from torchvision.models import (
    resnet18,
    ResNet18_Weights
)


# =========================
# 1. 选择运行设备
# =========================

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(
    "device:",
    device
)


# =========================
# 2. 数据路径
# =========================

train_path = (
    "data/industrial_classification/train"
)

val_path = (
    "data/industrial_classification/val"
)


# =========================
# 3. ResNet18预训练权重
# =========================

weights = ResNet18_Weights.DEFAULT


# =========================
# 4. 训练集数据增强
# =========================

train_transform = transforms.Compose(
    [
        transforms.RandomResizedCrop(
            224,
            scale=(
                0.8,
                1.0
            )
        ),

        transforms.RandomHorizontalFlip(
            p=0.5
        ),

        transforms.RandomRotation(
            degrees=10
        ),

        transforms.ColorJitter(
            brightness=0.2,
            contrast=0.2
        ),

        transforms.ToTensor(),

        transforms.Normalize(
            mean=[
                0.485,
                0.456,
                0.406
            ],
            std=[
                0.229,
                0.224,
                0.225
            ]
        )
    ]
)


# =========================
# 5. 验证集预处理
# =========================

val_transform = (
    weights.transforms()
)


# =========================
# 6. Dataset
# =========================

train_dataset = datasets.ImageFolder(
    root=train_path,
    transform=train_transform
)

val_dataset = datasets.ImageFolder(
    root=val_path,
    transform=val_transform
)


print(
    "train size:",
    len(train_dataset)
)

print(
    "val size:",
    len(val_dataset)
)

print(
    "class_to_idx:",
    train_dataset.class_to_idx
)


# =========================
# 7. DataLoader
# =========================

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=32,
    shuffle=False
)


# =========================
# 8. 加载预训练ResNet18
# =========================

model = resnet18(
    weights=weights
)


# =========================
# 9. 冻结原始参数
# =========================

for parameter in model.parameters():

    parameter.requires_grad = False


# =========================
# 10. 替换六分类Head
# =========================

input_features = (
    model.fc.in_features
)

model.fc = nn.Linear(
    input_features,
    6
)


print(
    "new fc:",
    model.fc
)


# =========================
# 11. 查看可训练参数
# =========================

print(
    "\nTrainable parameters:"
)

for name, parameter in model.named_parameters():

    if parameter.requires_grad:

        print(
            name,
            parameter.shape
        )


# =========================
# 12. 模型放到GPU/CPU
# =========================

model = model.to(device)


# =========================
# 13. Loss
# =========================

criterion = nn.CrossEntropyLoss()


# =========================
# 14. Optimizer
# 只更新requires_grad=True的参数
# =========================

optimizer = torch.optim.Adam(
    filter(
        lambda parameter:
            parameter.requires_grad,
        model.parameters()
    ),
    lr=0.001
)


# =========================
# 15. 单个Epoch训练函数
# =========================

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

    for images, labels in loader:

        # 图片和标签搬到GPU
        images = images.to(device)
        labels = labels.to(device)

        # 清空上一Batch梯度
        optimizer.zero_grad()

        # Forward
        logits = model(
            images
        )

        # Loss
        loss = criterion(
            logits,
            labels
        )

        # 计算梯度
        loss.backward()

        # 修改参数
        optimizer.step()

        # 预测类别
        predicted_classes = torch.argmax(
            logits,
            dim=1
        )

        # 统计正确数量
        correct += (
            predicted_classes
            == labels
        ).sum().item()

        # 统计样本数量
        total += labels.size(0)

        # 累计Loss
        total_loss += (
            loss.item()
            * images.size(0)
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


# =========================
# 16. 验证函数
# =========================

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

        for images, labels in loader:

            images = images.to(device)
            labels = labels.to(device)

            # Forward
            logits = model(
                images
            )

            # Loss
            loss = criterion(
                logits,
                labels
            )

            # 类别预测
            predicted_classes = torch.argmax(
                logits,
                dim=1
            )

            # 正确数量
            correct += (
                predicted_classes
                == labels
            ).sum().item()

            # 样本数量
            total += labels.size(0)

            # 累计Loss
            total_loss += (
                loss.item()
                * images.size(0)
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


# =========================
# 17. 模型保存目录
# =========================

os.makedirs(
    "models",
    exist_ok=True
)


best_model_path = (
    "models/day104_best_industrial_resnet.pth"
)

best_val_accuracy = 0.0


# =========================
# 18. 开始训练
# =========================

epochs = 10


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

    val_loss, val_accuracy = (
        evaluate(
            model,
            val_loader,
            criterion,
            device
        )
    )

    print(
        f"Epoch {epoch + 1}",
        f"train loss={train_loss:.4f}",
        f"train acc={train_accuracy:.4f}",
        f"val loss={val_loss:.4f}",
        f"val acc={val_accuracy:.4f}"
    )

    # =========================
    # 保存验证集表现最好的模型
    # =========================

    if (
        val_accuracy
        > best_val_accuracy
    ):

        best_val_accuracy = (
            val_accuracy
        )

        torch.save(
            model.state_dict(),
            best_model_path
        )

        print(
            "保存新的 best model:",
            best_val_accuracy
        )


print(
    "training finished"
)


# =========================
# 19. 创建新的ResNet18
# =========================

best_model = resnet18(
    weights=None
)


# =========================
# 20. 同样改成六分类
# =========================

best_model.fc = nn.Linear(
    best_model.fc.in_features,
    6
)


# =========================
# 21. 加载best checkpoint
# =========================

state_dict = torch.load(
    best_model_path,
    map_location=device
)

best_model.load_state_dict(
    state_dict
)


# =========================
# 22. 模型放到device
# =========================

best_model = best_model.to(device)


# =========================
# 23. 切换评估模式
# =========================

best_model.eval()


# =========================
# 24. 最终验证best model
# =========================

best_loss, best_accuracy = (
    evaluate(
        best_model,
        val_loader,
        criterion,
        device
    )
)


print(
    "best model loss:",
    best_loss
)

print(
    "best model accuracy:",
    best_accuracy
)