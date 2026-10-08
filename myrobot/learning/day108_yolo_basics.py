from ultralytics import YOLO


# =========================
# 1. 加载预训练YOLO模型
# =========================

model = YOLO(
    "yolov8n.pt"
)


# =========================
# 2. 测试图片
# =========================

image_path = (
    "images/yolo_test.jpg"
)


# =========================
# 3. 模型推理
# =========================

results = model(
    image_path
)


# =========================
# 4. 取第一张图片结果
# =========================

result = results[0]


# =========================
# 5. 所有Bounding Boxes
# =========================

boxes = result.boxes


print(
    "number of detections:",
    len(boxes)
)


# =========================
# 6. 遍历检测结果
# =========================

for index, box in enumerate(boxes):

    # -------------------------
    # Bounding Box
    # [x1, y1, x2, y2]
    # -------------------------

    xyxy = (
        box.xyxy[0]
        .cpu()
        .tolist()
    )

    x1, y1, x2, y2 = (
        xyxy
    )


    # -------------------------
    # Confidence
    # -------------------------

    confidence = (
        box.conf[0]
        .item()
    )


    # -------------------------
    # Class ID
    # -------------------------

    class_id = int(
        box.cls[0]
        .item()
    )


    # -------------------------
    # Class Name
    # -------------------------

    class_name = (
        model.names[
            class_id
        ]
    )


    # -------------------------
    # Bounding Box Center
    # -------------------------

    center_x = (
        x1 + x2
    ) / 2

    center_y = (
        y1 + y2
    ) / 2


    # -------------------------
    # 输出
    # -------------------------

    print(
        "\nDetection:",
        index
    )

    print(
        "class id:",
        class_id
    )

    print(
        "class name:",
        class_name
    )

    print(
        "confidence:",
        confidence
    )

    print(
        "bounding box:",
        xyxy
    )

    print(
        "center:",
        (
            center_x,
            center_y
        )
    )


# =========================
# 7. 保存画框后的图片
# =========================

result.save(
    filename=(
        "images/yolo_result.jpg"
    )
)


print(
    "\nresult saved:"
)

print(
    "images/yolo_result.jpg"
)