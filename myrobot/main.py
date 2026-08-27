from robot.robot import Robot

from vision.camera import Camera
from vision.image_processor import ImageProcessor
from vision.detector import Detector

from planner.task_planner import TaskPlanner
from controller.robot_controller import RobotController


def main():

    # =========================
    # 1. 创建系统对象
    # =========================

    camera = Camera()

    robot = Robot(
        "A01",
        80
    )

    planner = TaskPlanner(
        position_tolerance=5,
        required_stable_frames=3
    )

    controller = RobotController()


    # =========================
    # 2. 模拟连续摄像头帧
    # =========================

    image_paths = [
        "images/frame1.png",
        "images/frame2.png",
        "images/frame3.png",
        "images/frame4.png"
    ]


    # =========================
    # 3. 一帧一帧处理
    # =========================

    for frame_number, image_path in enumerate(
        image_paths,
        start=1
    ):

        print(
            f"\n===== 第 {frame_number} 帧 ====="
        )


        # =====================
        # 4. 获取当前帧
        # =====================

        image = camera.capture(
            image_path
        )


        if image is None:

            print(
                "当前帧读取失败"
            )

            planner.reset_tracking()

            continue


        # =====================
        # 5. resize
        # =====================

        resized_image = (
            ImageProcessor.resize(
                image,
                640,
                480
            )
        )


        # =====================
        # 6. 灰度化
        # =====================

        gray_image = (
            ImageProcessor.to_gray(
                resized_image
            )
        )


        # =====================
        # 7. 二值化
        # =====================

        binary_image = (
            ImageProcessor.threshold(
                gray_image,
                220
            )
        )


        # =====================
        # 8. 找轮廓
        # =====================

        contours = (
            Detector.find_contours(
                binary_image
            )
        )


        # =====================
        # 9. 过滤小轮廓
        # =====================

        valid_contours = (
            Detector.filter_contours(
                contours,
                min_area=100
            )
        )


        # =====================
        # 10. 分析轮廓
        # =====================

        results = []

        for contour in valid_contours:

            result = (
                Detector.analyze_contour(
                    contour
                )
            )

            if result is not None:

                results.append(
                    result
                )


        # =====================
        # 11. Planner选择目标
        # =====================

        selected_target = (
            planner.select_target(
                results
            )
        )


        # =====================
        # 12. Day64核心
        # 目标丢失 → 重置状态
        # =====================

        if selected_target is None:

            print(
                "当前帧目标丢失"
            )

            planner.reset_tracking()

            continue


        # =====================
        # 13. 判断当前目标稳定性
        # =====================

        stable = (
            planner.is_target_stable(
                selected_target
            )
        )


        print(
            "当前稳定判断：",
            stable
        )


        # =====================
        # 14. 稳定后执行移动
        # =====================

        if stable:

            controller.move_to_target(
                robot,
                selected_target
            )

            break


if __name__ == "__main__":

    main()