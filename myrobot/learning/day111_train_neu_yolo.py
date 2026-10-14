from ultralytics import YOLO


def main():

    # =========================
    # 1. 加载预训练YOLO
    # =========================

    model = YOLO(
        "yolov8n.pt"
    )


    print(
        "Start NEU-DET training..."
    )


    # =========================
    # 2. 工业缺陷迁移学习
    # =========================

    train_results = model.train(
        data="data/neu_det.yaml",
        epochs=20,
        imgsz=640,
        batch=8,
        device=0,
        project="runs/day111",
        name="neu_det_training"
    )


    print(
        "Training finished."
    )


    # =========================
    # 3. 获取真实best.pt路径
    # =========================

    best_model_path = (
        model.trainer.best
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


if __name__ == "__main__":
    main()