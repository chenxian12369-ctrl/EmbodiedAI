import torch

from torch.utils.data import DataLoader

from torchvision import datasets

from torchvision.models import (
    ResNet18_Weights
)


weights = ResNet18_Weights.DEFAULT

transform = weights.transforms()


dataset_path = (
    "data/industrial_classification"
)


dataset = datasets.ImageFolder(
    root=dataset_path,
    transform=transform
)


print(
    "dataset size:",
    len(dataset)
)

print(
    "classes:",
    dataset.classes
)

print(
    "class_to_idx:",
    dataset.class_to_idx
)


image, label = dataset[0]


print(
    "single image shape:",
    image.shape
)

print(
    "single label:",
    label
)


loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)


for images, labels in loader:

    print(
        "batch images:",
        images.shape
    )

    print(
        "batch labels:",
        labels.shape
    )

    print(
        "labels:",
        labels
    )

    break