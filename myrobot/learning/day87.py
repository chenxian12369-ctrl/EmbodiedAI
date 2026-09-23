import torch

x = torch.tensor(
    2.0,
    requires_grad=True
)

y = x ** 2

print(
    "x:",
    x
)

print(
    "y:",
    y
)
x = torch.tensor(
    3.0,
    requires_grad=True
)

a = x * 2

y = a ** 2

y.backward()

print(
    "x.grad:",
    x.grad
)

weight = torch.tensor(
    2.0,
    requires_grad=True
)

x = torch.tensor(
    3.0
)

target = torch.tensor(
    10.0
)

prediction = weight * x

loss = (
    prediction - target
) ** 2

print(
    "prediction:",
    prediction
)

print(
    "loss:",
    loss
)

loss.backward()

print(
    "weight.grad:",
    weight.grad
)

learning_rate = 0.1

with torch.no_grad():

    weight -= (
        learning_rate
        * weight.grad
    )

print(
    "updated weight:",
    weight
)
weight.grad.zero_()

prediction = weight * x

loss = (
    prediction - target
) ** 2

loss.backward()

weight = torch.tensor(
    2.0,
    requires_grad=True
)

x = torch.tensor(
    3.0
)

target = torch.tensor(
    10.0
)

learning_rate = 0.01


for step in range(10):

    # 1. 前向预测
    prediction = (
        weight * x
    )

    # 2. 计算loss
    loss = (
        prediction - target
    ) ** 2

    # 3. 清空旧梯度
    if weight.grad is not None:
        weight.grad.zero_()

    # 4. 反向传播
    loss.backward()

    # 5. 更新参数
    with torch.no_grad():

        weight -= (
            learning_rate
            * weight.grad
        )

    print(
        f"step={step}",
        f"weight={weight.item():.4f}",
        f"prediction={prediction.item():.4f}",
        f"loss={loss.item():.4f}",
        f"grad={weight.grad.item():.4f}"
    )