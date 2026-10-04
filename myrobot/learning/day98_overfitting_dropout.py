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

# validation_dataset = datasets.MNIST(
#     root="data",
#     train=False,
#     download=True,
#     transform=transform
# )

# train_loader = DataLoader(
#     train_dataset,
#     batch_size=64,
#     shuffle=True
# )

# validation_loader = DataLoader(
#     validation_dataset,
#     batch_size=64,
#     shuffle=False
# )
# class MNISTCNNWithDropout(nn.Module):

#     def __init__(self):

#         super().__init__()

#         self.conv1 = nn.Conv2d(
#             1,
#             8,
#             kernel_size=3,
#             padding=1
#         )

#         self.relu1 = nn.ReLU()

#         self.pool1 = nn.MaxPool2d(
#             2,
#             2
#         )

#         self.conv2 = nn.Conv2d(
#             8,
#             16,
#             kernel_size=3,
#             padding=1
#         )

#         self.relu2 = nn.ReLU()

#         self.pool2 = nn.MaxPool2d(
#             2,
#             2
#         )

#         self.flatten = nn.Flatten()

#         # 🔴【新增】
#         self.dropout = nn.Dropout(
#             p=0.5
#         )

#         self.fc = nn.Linear(
#             16 * 7 * 7,
#             10
#         )

#     def forward(
#         self,
#         x
#     ):

#         x = self.conv1(x)
#         x = self.relu1(x)
#         x = self.pool1(x)

#         x = self.conv2(x)
#         x = self.relu2(x)
#         x = self.pool2(x)

#         x = self.flatten(x)

#         # 🔴【新增】
#         x = self.dropout(x)

#         x = self.fc(x)

#         return x
# model = MNISTCNNWithDropout()

# criterion = nn.CrossEntropyLoss()

# optimizer = torch.optim.Adam(
#     model.parameters(),
#     lr=0.001
# )

# epochs = 5
# for epoch in range(epochs):

#     model.train()

#     total_train_loss = 0.0
#     train_correct = 0
#     train_total = 0

#     for batch_x, batch_target in train_loader:

#         optimizer.zero_grad()

#         logits = model(
#             batch_x
#         )

#         loss = criterion(
#             logits,
#             batch_target
#         )

#         loss.backward()

#         optimizer.step()

#         predicted_classes = torch.argmax(
#             logits,
#             dim=1
#         )

#         train_correct += (
#             predicted_classes
#             == batch_target
#         ).sum().item()

#         train_total += (
#             batch_target.size(0)
#         )

#         total_train_loss += (
#             loss.item()
#             * batch_x.size(0)
#         )

#     average_train_loss = (
#         total_train_loss
#         / len(train_dataset)
#     )

#     train_accuracy = (
#         train_correct
#         / train_total
#     )
#     model.eval()

#     total_validation_loss = 0.0
#     validation_correct = 0
#     validation_total = 0

#     with torch.no_grad():

#         for batch_x, batch_target in validation_loader:

#             logits = model(
#                 batch_x
#             )

#             loss = criterion(
#                 logits,
#                 batch_target
#             )

#             predicted_classes = torch.argmax(
#                 logits,
#                 dim=1
#             )

#             validation_correct += (
#                 predicted_classes
#                 == batch_target
#             ).sum().item()

#             validation_total += (
#                 batch_target.size(0)
#             )

#             total_validation_loss += (
#                 loss.item()
#                 * batch_x.size(0)
#             )

#     average_validation_loss = (
#         total_validation_loss
#         / len(validation_dataset)
#     )

#     validation_accuracy = (
#         validation_correct
#         / validation_total
#     )

#     print(
#         f"Epoch {epoch + 1}",
#         f"train loss={average_train_loss:.4f}",
#         f"train acc={train_accuracy:.4f}",
#         f"val loss={average_validation_loss:.4f}",
#         f"val acc={validation_accuracy:.4f}"
#     )