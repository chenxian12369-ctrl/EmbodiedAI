import torch
import torch.nn as nn
conv = nn.Conv2d(
    in_channels=1,
    out_channels=4,
    kernel_size=3
)

print(conv)
image = torch.randn(
    1,
    1,
    28,
    28
)

output = conv(image)

print(
    "input shape:",
    image.shape
)

print(
    "output shape:",
    output.shape
)
conv_stride2 = nn.Conv2d(
    in_channels=1,
    out_channels=4,
    kernel_size=3,
    stride=2
)

output = conv_stride2(
    image
)

print(
    "stride=2 output:",
    output.shape
)

conv_padding = nn.Conv2d(
    in_channels=1,
    out_channels=4,
    kernel_size=3,
    stride=1,
    padding=1
)

output = conv_padding(
    image
)

print(
    "padding output:",
    output.shape
)
conv_rgb = nn.Conv2d(
    in_channels=3,
    out_channels=16,
    kernel_size=3
)
class SmallCNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.conv = nn.Conv2d(
            in_channels=1,
            out_channels=8,
            kernel_size=3,
            stride=1,
            padding=1
        )

        self.relu = nn.ReLU()

    def forward(
        self,
        x
    ):

        print(
            "输入：",
            x.shape
        )

        x = self.conv(x)

        print(
            "Conv之后：",
            x.shape
        )

        x = self.relu(x)

        print(
            "ReLU之后：",
            x.shape
        )

        return x
model = SmallCNN()

images = torch.randn(
    32,
    1,
    28,
    28
)

output = model(
    images
)