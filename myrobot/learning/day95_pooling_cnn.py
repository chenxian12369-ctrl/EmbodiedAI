# import torch
# import torch.nn as nn

# x = torch.randn(
#     1,
#     8,
#     28,
#     28
# )

# pool = nn.MaxPool2d(
#     kernel_size=2,
#     stride=2
# )

# output = pool(x)

# print(
#     "input:",
#     x.shape
# )

# print(
#     "output:",
#     output.shape
# )

# class SmallCNN(nn.Module):

#     def __init__(self):

#         super().__init__()

#         self.conv1 = nn.Conv2d(
#             in_channels=1,
#             out_channels=8,
#             kernel_size=3,
#             padding=1
#         )

#         self.relu1 = nn.ReLU()

#         self.pool1 = nn.MaxPool2d(
#             kernel_size=2,
#             stride=2
#         )

#         self.conv2 = nn.Conv2d(
#             in_channels=8,
#             out_channels=16,
#             kernel_size=3,
#             padding=1
#         )

#         self.relu2 = nn.ReLU()

#         self.pool2 = nn.MaxPool2d(
#             kernel_size=2,
#             stride=2
#         )

#         self.flatten = nn.Flatten()

#         self.fc = nn.Linear(
#             16 * 7 * 7,
#             10
#         )
#     def forward(
#     self,
#     x
# ):

#         print(
#             "输入:",
#             x.shape
#         )

#         x = self.conv1(x)

#         print(
#             "conv1:",
#             x.shape
#         )

#         x = self.relu1(x)

#         x = self.pool1(x)

#         print(
#             "pool1:",
#             x.shape
#         )

#         x = self.conv2(x)

#         print(
#             "conv2:",
#             x.shape
#         )

#         x = self.relu2(x)

#         x = self.pool2(x)

#         print(
#             "pool2:",
#             x.shape
#         )

#         x = self.flatten(x)

#         print(
#             "flatten:",
#             x.shape
#         )

#         x = self.fc(x)

#         print(
#             "fc:",
#             x.shape
#         )

#         return x
# model = SmallCNN()

# images = torch.randn(
#     32,
#     1,
#     28,
#     28
# )

# output = model(
#     images
# )
# for name, parameter in model.named_parameters():

#     print(
#         name,
#         parameter.shape
#     )