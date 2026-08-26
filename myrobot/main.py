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
    # 2. 获取图片
    # =========================

    image = camera.capture(
        "images/test.jpg"
    )

    if image is None:

        print(
            "图片读取失败"
        )

        return


    # =========================
    # 3. 图像预处理
    # =========================

    resized_image = (
        ImageProcessor.resize(
            image,
            640,
            480
        )
    )


    gray_image = (
        ImageProcessor.to_gray(
            resized_image
        )
    )


    binary_image = (
        ImageProcessor.threshold(
            gray_image,
            220
        )
    )


    # =========================
    # 4. 查找轮廓
    # =========================

    contours = (
        Detector.find_contours(
            binary_image
        )
    )


    # =========================
    # 5. 过滤小轮廓
    # =========================

    valid_contours = (
        Detector.filter_contours(
            contours,
            min_area=100
        )
    )


    # =========================
    # 6. 将轮廓转换成检测结果
    # =========================

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


    # =========================
    # 7. TaskPlanner选择目标
    # =========================

    selected_target = (
        planner.select_target(
            results
        )
    )


    # 没有目标时直接结束
    if selected_target is None:

        return


    # =========================
    # 8. Day63
    # 模拟连续摄像头帧
    # =========================

    for frame in range(4):

        stable = (
            planner.is_target_stable(
                selected_target
            )
        )


        print(
            f"第{frame + 1}次检测：",
            stable
        )


        # =====================
        # 目标连续稳定后
        # 才允许机器人移动
        # =====================

        if stable:

            controller.move_to_target(
                robot,
                selected_target
            )

            break


if __name__ == "__main__":

    main()