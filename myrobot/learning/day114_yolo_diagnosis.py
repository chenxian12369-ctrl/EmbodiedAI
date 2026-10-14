from pathlib import Path

from ultralytics import YOLO


def main():

    # =========================
    # 1. 搜索best.pt
    # =========================

    runs_root = Path(
        "runs"
    )

    best_model_files = list(
        runs_root.glob(
            "**/day111/**/weights/best.pt"
        )
    )

    if len(
        best_model_files
    ) == 0:

        raise FileNotFoundError(
            "没有找到Day111训练生成的best.pt"
        )


    # =========================
    # 2. 最新best.pt
    # =========================

    best_model_path = max(
        best_model_files,
        key=lambda path:
            path.stat().st_mtime
    )


    print(
        "Best model:",
        best_model_path
    )


    # =========================
    # 3. 加载模型
    # =========================

    model = YOLO(
        str(
            best_model_path
        )
    )


    # =========================
    # 4. Validation
    # =========================

    metrics = model.val(
        data="data/neu_det.yaml",
        split="val",
        device=0,
        plots=True,
        workers=0
    )


    # =========================
    # 5. Overall Metrics
    # =========================

    print(
        "\n===== Overall Metrics ====="
    )

    print(
        "Precision:",
        metrics.box.mp
    )

    print(
        "Recall:",
        metrics.box.mr
    )

    print(
        "mAP50:",
        metrics.box.map50
    )

    print(
        "mAP50-95:",
        metrics.box.map
    )


    # =========================
    # 6. Per-class Metrics
    # =========================

    print(
        "\n===== Per-class Metrics ====="
    )


    number_of_classes = len(
        model.names
    )


    for class_id in range(
        number_of_classes
    ):

        class_name = (
            model.names[
                class_id
            ]
        )


        (
            precision,
            recall,
            ap50,
            ap50_95
        ) = metrics.class_result(
            class_id
        )


        print(
            "\nClass:",
            class_name
        )

        print(
            "Precision:",
            precision
        )

        print(
            "Recall:",
            recall
        )

        print(
            "AP50:",
            ap50
        )

        print(
            "AP50-95:",
            ap50_95
        )


    print(
        "\nResults saved to:",
        metrics.save_dir
    )


if __name__ == "__main__":
    main()