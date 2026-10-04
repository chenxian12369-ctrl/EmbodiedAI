# import torch
# import torch.nn as nn

# from torch.utils.data import DataLoader

# from torchvision import (
#     datasets,
#     transforms
# )
# transform = transforms.ToTensor()

# train_dataset = datasets.MNIST(
#     root="data",
#     train=True,
#     download=True,
#     transform=transform
# )



# test_dataset = datasets.MNIST(
#     root="data",
#     train=False,
#     download=True,
#     transform=transform
# )

# print(
#     "train size:",
#     len(train_dataset)
# )

# print(
#     "test size:",
#     len(test_dataset)
# )

# image, label = train_dataset[0]

# print(
#     "image shape:",
#     image.shape
# )

# print(
#     "label:",
#     label
# )
# train_loader = DataLoader(
#     train_dataset,
#     batch_size=64,
#     shuffle=True
# )

# test_loader = DataLoader(
#     test_dataset,
#     batch_size=64,
#     shuffle=False
# )

# for batch_images, batch_labels in train_loader:

#     print(
#         "batch images:",
#         batch_images.shape
#     )

#     print(
#         "batch labels:",
#         batch_labels.shape
#     )

#     break
# class MNISTNetwork(nn.Module):

#     def __init__(self):

#         super().__init__()

#         self.fc1 = nn.Linear(
#             784,
#             128
#         )

#         self.relu = nn.ReLU()

#         self.fc2 = nn.Linear(
#             128,
#             10
#         )

#     def forward(
#         self,
#         x
#     ):

#         x = x.reshape(
#             x.size(0),
#             -1
#         )

#         x = self.fc1(x)

#         x = self.relu(x)

#         x = self.fc2(x)

#         return x
# model = MNISTNetwork()
# criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(
#     model.parameters(),
#     lr=0.1
# )
# epochs = 3
# for epoch in range(epochs):

#     model.train()

#     total_loss = 0.0

#     correct_count = 0

#     total_count = 0

#     for images, labels in train_loader:

#         optimizer.zero_grad()

#         logits = model(
#             images
#         )

#         loss = criterion(
#             logits,
#             labels
#         )

#         loss.backward()

#         optimizer.step()

#         total_loss += (
#             loss.item()
#             * images.size(0)
#         )

#         predicted = torch.argmax(
#             logits,
#             dim=1
#         )

#         correct_count += (
#             predicted
#             == labels
#         ).sum().item()

#         total_count += (
#             labels.size(0)
#         )
#     train_loss = (
#         total_loss
#         / len(train_dataset)
#     )

#     train_accuracy = (
#         correct_count
#         / total_count
#     )
#     model.eval()

#     test_correct = 0

#     test_total = 0
#     with torch.no_grad():

#         for images, labels in test_loader:

#             logits = model(
#                 images
#             )

#             predicted = torch.argmax(
#                 logits,
#                 dim=1
#             )

#             test_correct += (
#                 predicted
#                 == labels
#             ).sum().item()

#             test_total += (
#                 labels.size(0)
#             )
#     test_accuracy = (
#         test_correct
#         / test_total
#     )
#     print(
#         f"Epoch {epoch + 1}",
#         f"train loss={train_loss:.4f}",
#         f"train acc={train_accuracy:.4f}",
#         f"test acc={test_accuracy:.4f}"
#     )