import torch

from torch.utils.data import DataLoader

from torchvision import (
    datasets,
    transforms
)

from torchvision.models import (
    ResNet18_Weights
)


train_path = (
    "data/industrial_classification/train"
)

val_path = (
    "data/industrial_classification/val"
)


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


weights = ResNet18_Weights.DEFAULT

val_transform = (
    weights.transforms()
)


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
    "train class_to_idx:",
    train_dataset.class_to_idx
)

print(
    "val class_to_idx:",
    val_dataset.class_to_idx
)


train_loader = DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=4,
    shuffle=False
)


for images, labels in train_loader:

    print(
        "train images:",
        images.shape
    )

    print(
        "train labels:",
        labels
    )

    break


for images, labels in val_loader:

    print(
        "val images:",
        images.shape
    )

    print(
        "val labels:",
        labels
    )

    break


image1, label1 = (
    train_dataset[0]
)

image2, label2 = (
    train_dataset[0]
)

difference = (
    image1
    - image2
).abs().mean()


print(
    "same labels:",
    label1,
    label2
)

print(
    "augmentation difference:",
    difference.item()
)