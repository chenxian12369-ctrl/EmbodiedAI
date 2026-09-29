# import torch
# import torch.nn as nn

# class ClassificationNetwork(nn.Module):

#     def __init__(self):

#         super().__init__()

#         self.fc1 = nn.Linear(
#             20,
#             32
#         )

#         self.relu = nn.ReLU()

#         self.fc2 = nn.Linear(
#             32,
#             4
#         )

#     def forward(
#         self,
#         x
#     ):

#         x = self.fc1(x)

#         x = self.relu(x)

#         x = self.fc2(x)

#         return x
# x = torch.randn(
#     1,
#     20
# )

# model = ClassificationNetwork()

# output = model(x)

# print(
#     output
# )

# print(
#     output.shape
# )

# output = model(x)

# print(
#     "output shape:",
#     output.shape
# )


# print(
#     "classification loss:",
#     loss.item()
# )

# predicted_classes = torch.argmax(
#     output,
#     dim=1
# )

# print(
#     "预测：",
#     predicted_classes
# )

# print(
#     "真实：",
#     target
# )
# correct = (
#     predicted_classes
#     == target
# )
# accuracy = (
#     correct.float().mean()
# )
# print(
#     "accuracy:",
#     accuracy.item()
# )

