from ultralytics import YOLO


# =========================
# 1. 加载预训练YOLO
# =========================

model = YOLO(
    "yolov8n.pt"
)


print(
    "Start YOLO training..."
)


# =========================
# 2. 训练
# =========================

train_results = model.train(
    data="coco8.yaml",
    epochs=10,
    imgsz=640,
    batch=8,
    device=0,
    project="runs/day109",
    name="coco8_training"
)


print(
    "Training finished."
)


# =========================
# 3. best模型路径
# =========================

best_model_path = (
    "runs/day109/"
    "coco8_training/"
    "weights/best.pt"
)


print(
    "Best model path:",
    best_model_path
)


# =========================
# 4. 加载best model
# =========================

best_model = YOLO(
    best_model_path
)


# =========================
# 5. Validation
# =========================

print(
    "Start validation..."
)


metrics = best_model.val()


print(
    "Validation finished."
)


# =========================
# 6. 使用自己的best模型推理
# =========================

prediction_results = best_model(
    "images/yolo_test.jpg"
)


result = prediction_results[0]


print(
    "number of detections:",
    len(result.boxes)
)


# =========================
# 7. 查看预测结果
# =========================

for index, box in enumerate(
    result.boxes
):

    class_id = int(
        box.cls[0].item()
    )

    class_name = (
        best_model.names[
            class_id
        ]
    )

    confidence = (
        box.conf[0].item()
    )

    xyxy = (
        box.xyxy[0]
        .cpu()
        .tolist()
    )

    print(
        "\nDetection:",
        index
    )

    print(
        "class:",
        class_name
    )

    print(
        "confidence:",
        confidence
    )

    print(
        "box:",
        xyxy
    )


# =========================
# 8. 保存推理结果
# =========================

result.save(
    filename=(
        "images/"
        "day109_yolo_result.jpg"
    )
)


print(
    "\nResult saved:"
)

print(
    "images/day109_yolo_result.jpg"
)