from robot.robot import Robot

from vision.camera import Camera
from vision.image_processor import ImageProcessor
from vision.detector import Detector

from planner.task_planner import TaskPlanner
from controller.robot_controller import RobotController
from vision.frame_source import ImageFrameSource
from vision.vision_pipeline import VisionPipeline

def main():

    # =========================
    # 1. 创建系统对象
    # =========================
    image_paths = [
        "images/frame1.png",
        "images/no.png",
        "images/frame3.png",
        "images/frame4.png"
    ]
    camera = Camera()
    frame_source = ImageFrameSource(
        camera,
        image_paths
    )
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




    # =========================
    # 3. 一帧一帧处理
    # =========================


    while True:
        image, finished, frame_number, error = (
    frame_source.get_next_frame()
)

        if finished:
            print("所有帧处理完成")
            break

        print(
    f"\n===== 第 {frame_number} 帧 ====="
)

        if image is None:

            # 🔴【修改】在帧标题之后再打印错误
            if error is not None:
                print(error)

            print("当前帧读取失败")

            planner.reset_tracking()

            continue

        # print(
        #     f"\n===== 第 {frame_number} 帧 ====="
        # )

        results = VisionPipeline.process_frame(
            image
        )

        selected_target = planner.select_target(
            results
        )

        if selected_target is None:

            print(
                "当前帧目标丢失"
            )

            planner.reset_tracking()

            continue


        stable = planner.is_target_stable(
            selected_target
        )

        print(
            "当前稳定判断：",
            stable
        )


        if stable:

            controller.move_to_target(
                robot,
                selected_target
            )

            break

if __name__ == "__main__":

    main()