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