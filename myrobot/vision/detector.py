import cv2
from vision.detection_result import DetectionResult

class Detector:


    @staticmethod
    def find_contours(binary_image):

        contours, hierarchy = cv2.findContours(

            binary_image,

            cv2.RETR_EXTERNAL,

            cv2.CHAIN_APPROX_SIMPLE

        )
        return contours
    @staticmethod
    def find_center(contour):
        """
        根据轮廓计算目标中心坐标
        """

        moments = cv2.moments(contour)

        if moments["m00"] == 0:
            return None

        center_x = int(
            moments["m10"] / moments["m00"]
        )

        center_y = int(
            moments["m01"] / moments["m00"]
        )

        return center_x, center_y
    @staticmethod
    def get_bounding_box(contour):
        """
        获取轮廓的外接矩形
        """

        x, y, width, height = cv2.boundingRect(
            contour
        )

        return x, y, width, height
    @staticmethod
    def analyze_contour(
        contour
    ):

        area = cv2.contourArea(
            contour
        )

        moments = cv2.moments(
            contour
        )

        if moments["m00"] == 0:
            return None


        cx = int(
            moments["m10"]
            /
            moments["m00"]
        )

        cy = int(
            moments["m01"]
            /
            moments["m00"]
        )

        center = (
            cx,
            cy
        )


        x, y, width, height = (
            cv2.boundingRect(
                contour
            )
        )

        bounding_box = (
            x,
            y,
            width,
            height
        )


        return DetectionResult(
            area,
            center,
            bounding_box
        )
    @staticmethod
    def filter_contours(contours, min_area=100):
        """
        过滤面积过小的轮廓
        """

        valid_contours = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area >= min_area:

                valid_contours.append(contour)

        return valid_contours