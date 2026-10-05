box_a = [
    100,
    100,
    300,
    300
]

box_b = [
    150,
    150,
    350,
    350
]
def calculate_iou(
    box_a,
    box_b
):

    ax1, ay1, ax2, ay2 = (
        box_a
    )

    bx1, by1, bx2, by2 = (
        box_b
    )


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
        intersection_x2
        - intersection_x1
    )

    intersection_height = max(
        0,
        intersection_y2
        - intersection_y1
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


    iou = (
        intersection_area
        / union_area
    )

    return iou

iou = calculate_iou(
    box_a,
    box_b
)

print(
    "box_a:",
    box_a
)

print(
    "box_b:",
    box_b
)

print(
    "IoU:",
    iou
)
box_c = [
    100,
    100,
    300,
    300
]

iou_same = calculate_iou(
    box_a,
    box_c
)

print(
    "same box IoU:",
    iou_same
)
box_d = [
    400,
    400,
    500,
    500
]

iou_none = calculate_iou(
    box_a,
    box_d
)

print(
    "no overlap IoU:",
    iou_none
)