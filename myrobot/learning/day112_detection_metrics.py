# =========================
# Day112
# Object Detection Metrics
# =========================


# 假设检测结果统计如下

true_positive = 80
false_positive = 10
false_negative = 20


# =========================
# 1. Precision
# =========================

precision = (
    true_positive
    /
    (
        true_positive
        + false_positive
    )
)


# =========================
# 2. Recall
# =========================

recall = (
    true_positive
    /
    (
        true_positive
        + false_negative
    )
)


print(
    "True Positive:",
    true_positive
)

print(
    "False Positive:",
    false_positive
)

print(
    "False Negative:",
    false_negative
)

print(
    "Precision:",
    precision
)

print(
    "Recall:",
    recall
)


# =========================
# 3. 模拟六个类别AP
# =========================

class_ap = {
    "crazing": 0.72,
    "inclusion": 0.81,
    "patches": 0.90,
    "pitted_surface": 0.76,
    "rolled-in_scale": 0.68,
    "scratches": 0.88
}


# =========================
# 4. 计算mAP
# =========================

total_ap = sum(
    class_ap.values()
)

number_of_classes = len(
    class_ap
)

mean_ap = (
    total_ap
    /
    number_of_classes
)


print(
    "\nClass AP:"
)

for class_name, ap in class_ap.items():

    print(
        class_name,
        ap
    )


print(
    "\nmAP:",
    mean_ap
)# =========================
# Day112
# Object Detection Metrics
# =========================


# 假设检测结果统计如下

true_positive = 80
false_positive = 10
false_negative = 20

