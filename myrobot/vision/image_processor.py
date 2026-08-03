import cv2


class ImageProcessor:

    @staticmethod
    def resize(image, width, height):
        """
        将图片缩放到指定宽度和高度
        """
        resized_image = cv2.resize(
            image,
            (width, height)
        )

        return resized_image

    @staticmethod
    def to_gray(image):
        """
        将BGR彩色图片转换成灰度图片
        """
        gray_image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        return gray_image

    @staticmethod
    def save(image, path):
        """
        将图片保存到指定路径
        """
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
    def crop(image, x1, y1, x2, y2):

        cropped_image = image[
            y1:y2,
            x1:x2
        ]

        return cropped_image