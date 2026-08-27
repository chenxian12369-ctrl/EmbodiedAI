from robot.robot import Robot

from vision.camera import Camera
from vision.image_processor import ImageProcessor
from vision.detector import Detector

from planner.task_planner import TaskPlanner
from controller.robot_controller import RobotController

from vision.vision_pipeline import VisionPipeline

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


        # =========================
        # 读取当前帧
        # =========================

        image = camera.capture(
            image_path
        )


        if image is None:

            print(
                "当前帧读取失败"
            )

            planner.reset_tracking()

            continue


        # =========================
        # Day65
        # 处理当前帧
        # =========================

        results =  VisionPipeline.process_frame(
            image
        )


        # =========================
        # Planner选择目标
        # =========================

        selected_target = planner.select_target(
            results
        )


        # =========================
        # 目标丢失
        # =========================

        if selected_target is None:

            print(
                "当前帧目标丢失"
            )

            planner.reset_tracking()

            continue


        # =========================
        # 稳定判断
        # =========================

        stable = planner.is_target_stable(
            selected_target
        )


        print(
            "当前稳定判断：",
            stable
        )


        # =========================
        # 执行动作
        # =========================

        if stable:

            controller.move_to_target(
                robot,
                selected_target
            )

            break

if __name__ == "__main__":

    main()