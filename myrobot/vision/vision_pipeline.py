from vision.image_processor import ImageProcessor
from vision.detector import Detector


class VisionPipeline:

    @staticmethod
    def process_frame(image):

        # =========================
        # 1. 图像缩放
        # =========================

        resized_image = ImageProcessor.resize(
            image,
            640,
            480
        )


        # =========================
        # 2. 灰度化
        # =========================

        gray_image = ImageProcessor.to_gray(
            resized_image
        )


        # =========================
        # 3. 二值化
        # =========================

        binary_image = ImageProcessor.threshold(
            gray_image,
            220
        )


        # =========================
        # 4. 查找轮廓
        # =========================

        contours = Detector.find_contours(
            binary_image
        )


        # =========================
        # 5. 过滤轮廓
        # =========================

        valid_contours = Detector.filter_contours(
            contours,
            min_area=100
        )


        # =========================
        # 6. 分析轮廓
        # =========================

        results = []

        for contour in valid_contours:

            result = Detector.analyze_contour(
                contour
            )

            if result is not None:

                results.append(
                    result
                )


        # =========================
        # 7. 返回所有检测结果
        # =========================

        return results