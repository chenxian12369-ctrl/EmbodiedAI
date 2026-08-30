import os

import cv2


class Camera:

    def capture(self, image_path):

        # =========================
        # 1. 先检查文件是否存在
        # =========================

        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"无法读取图片：{image_path}"
            )

        # =========================
        # 2. 读取图片
        # =========================

        image = cv2.imread(
            image_path
        )

        # =========================
        # 3. 文件存在，但图片无法解析
        # =========================

        if image is None:
            raise ValueError(
                f"图片文件存在，但无法解析：{image_path}"
            )

        return image