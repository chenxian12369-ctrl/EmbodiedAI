import cv2


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