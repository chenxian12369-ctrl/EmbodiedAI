import cv2


class ImageProcessor:

    @staticmethod
    def resize(image, width, height):

        resized_image = cv2.resize(
            image,
            (width, height)
        )

        return resized_image

    @staticmethod
    def to_gray(image):

        gray_image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        return gray_image

    @staticmethod
    def threshold(image, threshold_value=127):
        """
        将灰度图转换成黑白二值图
        """

        _, binary_image = cv2.threshold(
            image,
            threshold_value,
            255,
            cv2.THRESH_BINARY
        )

        return binary_image

    @staticmethod
    def detect_edges(image, low_threshold=100, high_threshold=200):
        """
        使用 Canny 算法检测图像边缘
        """

        edge_image = cv2.Canny(
            image,
            low_threshold,
            high_threshold
        )

        return edge_image

    @staticmethod
    def crop(image, x1, y1, x2, y2):

        cropped_image = image[
            y1:y2,
            x1:x2
        ]

        return cropped_image

    @staticmethod
    def save(image, path):

        success = cv2.imwrite(
            path,
            image
        )

        if not success:
            raise IOError(
                f"图片保存失败：{path}"
            )

        print(
            "图片保存成功：",
            path
        )