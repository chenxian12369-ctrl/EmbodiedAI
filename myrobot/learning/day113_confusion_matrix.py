# =========================
# Day113
# Confusion Matrix
# =========================


class_names = [
    "crazing",
    "inclusion",
    "scratches"
]


# =========================
# 1. 真实标签
# =========================

true_labels = [
    0,
    0,
    0,
    0,

    1,
    1,
    1,
    1,

    2,
    2,
    2,
    2
]


# =========================
# 2. 模型预测标签
# =========================

predicted_labels = [
    0,
    0,
    1,
    0,

    1,
    1,
    1,
    2,

    2,
    0,
    2,
    2
]


# =========================
# 3. 创建空混淆矩阵
# =========================

number_of_classes = len(
    class_names
)


confusion_matrix = [
    [
        0
        for _ in range(
            number_of_classes
        )
    ]

    for _ in range(
        number_of_classes
    )
]


# =========================
# 4. 填充矩阵
# =========================

for true_label, predicted_label in zip(
    true_labels,
    predicted_labels
):

    confusion_matrix[
        true_label
    ][
        predicted_label
    ] += 1


# =========================
# 5. 打印矩阵
# =========================

print(
    "Confusion Matrix:"
)


print(
    "True \\ Pred:",
    class_names
)


for index, row in enumerate(
    confusion_matrix
):

    print(
        class_names[index],
        row
    )


# =========================
# 6. 每类Recall
# =========================

print(
    "\nPer-class Recall:"
)


for class_id in range(
    number_of_classes
):

    true_positive = (
        confusion_matrix[
            class_id
        ][
            class_id
        ]
    )


    total_real = sum(
        confusion_matrix[
            class_id
        ]
    )


    recall = (
        true_positive
        / total_real
    )


    print(
        class_names[
            class_id
        ],
        recall
    )


# =========================
# 7. 总体Accuracy
# =========================

correct_predictions = 0


for class_id in range(
    number_of_classes
):

    correct_predictions += (
        confusion_matrix[
            class_id
        ][
            class_id
        ]
    )


total_samples = len(
    true_labels
)


accuracy = (
    correct_predictions
    /
    total_samples
)


print(
    "\nAccuracy:",
    accuracy
)