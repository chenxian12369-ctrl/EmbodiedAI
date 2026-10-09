import os
import xml.etree.ElementTree as ET


# =========================
# 1. 原始数据路径
# =========================

annotation_dir = (
    "data/NEU-DET/ANNOTATIONS"
)

output_label_dir = (
    "data/neu_det_yolo/labels"
)


os.makedirs(
    output_label_dir,
    exist_ok=True
)


# =========================
# 2. 类别映射
# =========================

class_to_id = {
    "crazing": 0,
    "inclusion": 1,
    "patches": 2,
    "pitted_surface": 3,
    "rolled-in_scale": 4,
    "scratches": 5
}


# =========================
# 3. xyxy → YOLO
# =========================

def convert_box_to_yolo(
    image_width,
    image_height,
    xmin,
    ymin,
    xmax,
    ymax
):

    box_width = (
        xmax
        - xmin
    )

    box_height = (
        ymax
        - ymin
    )


    center_x = (
        xmin
        + xmax
    ) / 2

    center_y = (
        ymin
        + ymax
    ) / 2


    normalized_center_x = (
        center_x
        / image_width
    )

    normalized_center_y = (
        center_y
        / image_height
    )

    normalized_width = (
        box_width
        / image_width
    )

    normalized_height = (
        box_height
        / image_height
    )


    return (
        normalized_center_x,
        normalized_center_y,
        normalized_width,
        normalized_height
    )


# =========================
# 4. 转换单个 XML
# =========================

def convert_xml(
    xml_path,
    output_txt_path
):

    tree = ET.parse(
        xml_path
    )

    root = tree.getroot()


    # -------------------------
    # 图片尺寸
    # -------------------------

    size = root.find(
        "size"
    )

    image_width = int(
        size.find(
            "width"
        ).text
    )

    image_height = int(
        size.find(
            "height"
        ).text
    )


    yolo_lines = []


    # -------------------------
    # 每一个目标
    # -------------------------

    for object_element in root.findall(
        "object"
    ):

        class_name = (
            object_element
            .find("name")
            .text
            .strip()
        )


        if (
            class_name
            not in class_to_id
        ):

            print(
                "Unknown class:",
                class_name
            )

            continue


        class_id = (
            class_to_id[
                class_name
            ]
        )


        bounding_box = (
            object_element
            .find("bndbox")
        )


        xmin = float(
            bounding_box
            .find("xmin")
            .text
        )

        ymin = float(
            bounding_box
            .find("ymin")
            .text
        )

        xmax = float(
            bounding_box
            .find("xmax")
            .text
        )

        ymax = float(
            bounding_box
            .find("ymax")
            .text
        )


        (
            center_x,
            center_y,
            box_width,
            box_height
        ) = convert_box_to_yolo(
            image_width,
            image_height,
            xmin,
            ymin,
            xmax,
            ymax
        )


        yolo_line = (
            f"{class_id} "
            f"{center_x:.6f} "
            f"{center_y:.6f} "
            f"{box_width:.6f} "
            f"{box_height:.6f}"
        )


        yolo_lines.append(
            yolo_line
        )


    # -------------------------
    # 写 txt
    # -------------------------

    with open(
        output_txt_path,
        "w",
        encoding="utf-8"
    ) as file:

        for line in yolo_lines:

            file.write(
                line
                + "\n"
            )


    return len(
        yolo_lines
    )


# =========================
# 5. 批量处理所有 XML
# =========================

xml_files = [
    filename
    for filename in os.listdir(
        annotation_dir
    )
    if filename.endswith(
        ".xml"
    )
]


print(
    "XML files:",
    len(xml_files)
)


total_objects = 0


for index, xml_filename in enumerate(
    xml_files
):

    xml_path = os.path.join(
        annotation_dir,
        xml_filename
    )


    txt_filename = (
        os.path.splitext(
            xml_filename
        )[0]
        + ".txt"
    )


    output_txt_path = os.path.join(
        output_label_dir,
        txt_filename
    )


    object_count = convert_xml(
        xml_path,
        output_txt_path
    )


    total_objects += (
        object_count
    )


    # 每100个打印一次
    if (
        (index + 1)
        % 100
        == 0
    ):

        print(
            "converted:",
            index + 1
        )


print(
    "Conversion finished."
)

print(
    "Total XML:",
    len(xml_files)
)

print(
    "Total objects:",
    total_objects
)

print(
    "YOLO labels saved to:",
    output_label_dir
)