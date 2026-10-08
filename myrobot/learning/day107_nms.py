def calculate_iou(
    box_a,
    box_b
):

    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b

    intersection_x1 = max(
        ax1,
        bx1
    )

    intersection_y1 = max(
        ay1,
        by1
    )

    intersection_x2 = min(
        ax2,
        bx2
    )

    intersection_y2 = min(
        ay2,
        by2
    )

    intersection_width = max(
        0,
        intersection_x2 - intersection_x1
    )

    intersection_height = max(
        0,
        intersection_y2 - intersection_y1
    )

    intersection_area = (
        intersection_width
        * intersection_height
    )

    area_a = (
        ax2 - ax1
    ) * (
        ay2 - ay1
    )

    area_b = (
        bx2 - bx1
    ) * (
        by2 - by1
    )

    union_area = (
        area_a
        + area_b
        - intersection_area
    )

    return (
        intersection_area
        / union_area
    )

detections = [
    {
        "class_name": "scratch",
        "confidence": 0.95,
        "box": [
            100,
            100,
            300,
            300
        ]
    },

    {
        "class_name": "scratch",
        "confidence": 0.88,
        "box": [
            120,
            120,
            310,
            310
        ]
    },

    {
        "class_name": "scratch",
        "confidence": 0.80,
        "box": [
            400,
            100,
            550,
            250
        ]
    }
]
def nms(
    detections,
    iou_threshold=0.5
):

    detections = sorted(
        detections,
        key=lambda detection:
            detection["confidence"],
        reverse=True
    )

    kept_detections = []

    while detections:

        best_detection = (
            detections.pop(0)
        )

        kept_detections.append(
            best_detection
        )

        remaining_detections = []

        for detection in detections:

            iou = calculate_iou(
                best_detection["box"],
                detection["box"]
            )

            if (
                iou
                < iou_threshold
            ):

                remaining_detections.append(
                    detection
                )

        detections = (
            remaining_detections
        )

    return kept_detections
kept = nms(
    detections,
    iou_threshold=0.5
)

print(
    "Before NMS:",
    len(detections)
)

print(
    "After NMS:",
    len(kept)
)

for detection in kept:

    print(
        detection
    )

