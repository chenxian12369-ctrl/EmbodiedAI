import os
import random
import shutil


# =========================
# 1. 原始路径
# =========================

source_image_dir = (
    "data/NEU-DET/IMAGES"
)

source_label_dir = (
    "data/neu_det_yolo/labels"
)


# =========================
# 2. 输出路径
# =========================

output_root = (
    "data/neu_det_yolo"
)

train_image_dir = os.path.join(
    output_root,
    "images",
    "train"
)

val_image_dir = os.path.join(
    output_root,
    "images",
    "val"
)

train_label_dir = os.path.join(
    output_root,
    "labels",
    "train"
)

val_label_dir = os.path.join(
    output_root,
    "labels",
    "val"
)


# =========================
# 3. 创建目录
# =========================

for directory in [
    train_image_dir,
    val_image_dir,
    train_label_dir,
    val_label_dir
]:

    os.makedirs(
        directory,
        exist_ok=True
    )


# =========================
# 4. 找到所有图片
# =========================

image_files = [
    filename
    for filename in os.listdir(
        source_image_dir
    )
    if filename.lower().endswith(
        (
            ".jpg",
            ".jpeg",
            ".png"
        )
    )
]


print(
    "Total images:",
    len(image_files)
)


# =========================
# 5. 固定随机种子
# =========================

random.seed(
    42
)


# =========================
# 6. 打乱图片顺序
# =========================

random.shuffle(
    image_files
)


# =========================
# 7. 80 / 20划分
# =========================

train_ratio = 0.8

split_index = int(
    len(image_files)
    * train_ratio
)


train_files = (
    image_files[
        :split_index
    ]
)

val_files = (
    image_files[
        split_index:
    ]
)


print(
    "Train images:",
    len(train_files)
)

print(
    "Val images:",
    len(val_files)
)


# =========================
# 8. 复制函数
# =========================

def copy_dataset_files(
    filenames,
    target_image_dir,
    target_label_dir
):

    copied_count = 0

    for image_filename in filenames:

        image_name_without_extension = (
            os.path.splitext(
                image_filename
            )[0]
        )

        label_filename = (
            image_name_without_extension
            + ".txt"
        )


        source_image_path = os.path.join(
            source_image_dir,
            image_filename
        )

        source_label_path = os.path.join(
            source_label_dir,
            label_filename
        )


        # =========================
        # 检查标签是否存在
        # =========================

        if not os.path.exists(
            source_label_path
        ):

            print(
                "Missing label:",
                source_label_path
            )

            continue


        target_image_path = os.path.join(
            target_image_dir,
            image_filename
        )

        target_label_path = os.path.join(
            target_label_dir,
            label_filename
        )


        shutil.copy2(
            source_image_path,
            target_image_path
        )

        shutil.copy2(
            source_label_path,
            target_label_path
        )


        copied_count += 1


    return copied_count


# =========================
# 9. 复制Train
# =========================

train_count = copy_dataset_files(
    train_files,
    train_image_dir,
    train_label_dir
)


# =========================
# 10. 复制Val
# =========================

val_count = copy_dataset_files(
    val_files,
    val_image_dir,
    val_label_dir
)


print(
    "Copied train:",
    train_count
)

print(
    "Copied val:",
    val_count
)

print(
    "Dataset preparation finished."
)