from robot.robot import Robot
from robot.robot_state import RobotState
from vision.camera import Camera
from vision.image_processor import ImageProcessor
from vision.detector import Detector
from vision.video_frame_source import VideoFrameSource
from planner.task_planner import TaskPlanner
from controller.robot_controller import RobotController
from vision.frame_source import ImageFrameSource
from vision.vision_pipeline import VisionPipeline
from robot.robot_state_machine import RobotStateMachine
def main():

    # =========================
    # 1. 创建系统对象
    # =========================

    camera = Camera()
# 🔴【新增】视频作为帧来源
    video_path = "videos/test.mp4"

    # 🔴【修改】不再使用 ImageFrameSource
    frame_source = VideoFrameSource(
        video_path
    )

    robot = Robot(
        "A01",
        80
    )

    planner = TaskPlanner(
        position_tolerance=5,
        required_stable_frames=3
    )

    controller = RobotController()
    print(
    controller.is_error_within_tolerance(
        (4, -3)
    )
)

    print(
        controller.is_error_within_tolerance(
            (6, 2)
        )
    )

    print(
        controller.is_error_within_tolerance(
            (-5, 5)
        )
    )

    print(
        controller.is_error_within_tolerance(
            (-7, -8)
        )
    )
# 🔴【新增】记录当前稳定目标是否已经执行过动作
# 🔴【新增】创建机器人状态机
    state_machine = RobotStateMachine()
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

        if frame_number % 20 == 0:
            print(
                f"已处理到第 {frame_number} 帧"
            )
        # 🔴【新增】ERROR 状态锁定 
        if state_machine.is_error(): 
        
            command = input( 
                "机器人处于 ERROR，输入 r 执行恢复：" 
            ) 
        
            if command == "r": 
        
                state_machine.recover() 
        
                planner.reset_tracking() 
        
            continue
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

    # 🔴【修改】先让状态机判断是不是真的丢失
            confirmed_lost = (
                state_machine.target_lost()
            )

            # 🔴【新增】只有连续丢失达到阈值才重置跟踪
            if confirmed_lost:

                print(
                    "确认目标丢失"
                )

                planner.reset_tracking()

            continue
        

        state_machine.target_found()
        stable = planner.is_target_stable(
            selected_target
        )

        # print(
        #     "当前稳定判断：",
        #     stable
        # )
        # 🔴【新增】Day68 状态机调试
        # print("当前机器人状态：", state.value)


        if stable:

            state_machine.target_stable()

            if state_machine.is_stable():

                print(
                    "机器人状态：",
                    state_machine.get_state().value
                )

                state_machine.start_moving()

                print(
                    "机器人状态：",
                    state_machine.get_state().value
                )

                controller.move_to_target(
                    robot,
                    selected_target
                )
                            
# 🔴【新增】视频处理结束后释放资源
    frame_source.release()
if __name__ == "__main__":

    main()