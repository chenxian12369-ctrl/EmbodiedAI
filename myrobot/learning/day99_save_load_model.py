import torch
import torch.nn as nn

class SimpleNetwork(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc1 = nn.Linear(
            10,
            16
        )

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(
            16,
            4
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
print(
    model.state_dict()
)
torch.save(
    model.state_dict(),
    "models/simple_model.pth"
)