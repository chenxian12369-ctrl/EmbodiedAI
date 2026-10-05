image_width = 640
image_height = 480


x1 = 100
y1 = 80

x2 = 300
y2 = 240


box_width = (
    x2
    - x1
)

box_height = (
    y2
    - y1
)

area = (
    box_width
    * box_height
)


center_x = (
    x1
    + x2
) / 2

center_y = (
    y1
    + y2
) / 2


class_name = "scratch"

confidence = 0.93


print(
    "image size:",
    image_width,
    image_height
)

print(
    "bounding box:",
    [
        x1,
        y1,
        x2,
        y2
    ]
)

print(
    "box width:",
    box_width
)

print(
    "box height:",
    box_height
)

print(
    "area:",
    area
)

print(
    "center:",
    (
        center_x,
        center_y
    )
)

print(
    "class:",
    class_name
)

print(
    "confidence:",
    confidence
)


class DetectionResult:

    def __init__(
        self,
        class_name,
        confidence,
        bounding_box
    ):

        self.class_name = (
            class_name
        )

        self.confidence = (
            confidence
        )

        self.bounding_box = (
            bounding_box
        )

    def get_center(
        self
    ):

        x1, y1, x2, y2 = (
            self.bounding_box
        )

        center_x = (
            x1
            + x2
        ) / 2

        center_y = (
            y1
            + y2
        ) / 2

        return (
            center_x,
            center_y
        )


result = DetectionResult(
    class_name="scratch",
    confidence=0.93,
    bounding_box=[
        100,
        80,
        300,
        240
    ]
)


print(
    "result class:",
    result.class_name
)

print(
    "result confidence:",
    result.confidence
)

print(
    "result box:",
    result.bounding_box
)

print(
    "result center:",
    result.get_center()
)