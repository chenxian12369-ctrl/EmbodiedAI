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
    def draw_bounding_box(
        image,
        bounding_box
    ):
        """
        在图片上绘制目标外接矩形
        """

        result = image.copy()

        x, y, width, height = bounding_box

        cv2.rectangle(
            result,
            (x, y),
            (x + width, y + height),
            (255, 0, 0),
            2
        )

        return result

    @staticmethod
    def crop(image, x1, y1, x2, y2):

        cropped_image = image[
            y1:y2,
            x1:x2
        ]

        return cropped_image
    @staticmethod
    def draw_center(image, center):
        """
        在图片上绘制目标中心点
        """

        result = image.copy()

        cv2.circle(
            result,
            center,
            5,
            (0, 0, 255),
            -1
        )
        return result

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
    @staticmethod
    def draw_contours(image, contours):

        result = image.copy()

        cv2.drawContours(

            result,

            contours,

            -1,

            (0,255,0),

            2

        )

        return result
    