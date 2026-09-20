from controller.pid_controller import (
    PIDController
)
class RobotController:
    def __init__(
    self,
    image_width=640,
    image_height=480,
    kp=0.1,
    ki=0.01,
    kd=0.5,
    control_tolerance=5
):

        self.image_center = (
            image_width // 2,
            image_height // 2
        )

        self.control_tolerance = (
            control_tolerance
        )

        # 🔴【新增】X轴 PID
        self.pid_x = PIDController(
            kp=kp,
            ki=ki,
            kd=kd,
            integral_limit=300
        )

        # 🔴【新增】Y轴 PID
        self.pid_y = PIDController(
            kp=kp,
            ki=ki,
            kd=kd,
            integral_limit=300
        )

    def calculate_visual_error(
        self,
        detection_result
    ):

        target_x, target_y = (
            detection_result.center
        )

        center_x, center_y = (
            self.image_center
        )

        error_x = (
            target_x - center_x
        )

        error_y = (
            target_y - center_y
        )

        return (
            error_x,
            error_y
        )
    def calculate_control(
    self,
    visual_error
):

        error_x, error_y = visual_error

        control_x = (
            self.pid_x.update(
                error_x
            )
        )

        control_y = (
            self.pid_y.update(
                error_y
            )
        )

        return (
            control_x,
            control_y
        )
    def is_error_within_tolerance(
        self,
        visual_error
    ):

        error_x, error_y = visual_error

        return (
            abs(error_x)
            <= self.control_tolerance
            and
            abs(error_y)
            <= self.control_tolerance
        )
    def reset_control(self):

        self.pid_x.reset()
        self.pid_y.reset()

        print(
            "PID控制器状态已重置"
        )
    def move_to_target(
        self,
        robot,
        detection_result
    ):


        if not detection_result.is_valid(500):
            print(
                "目标太小，忽略"
            )

            return False
        

        visual_error = (
    self.calculate_visual_error(
        detection_result
    )
)

        print(
            "视觉误差：",
            visual_error
        )

        # 🔴【先判断容差】
        if self.is_error_within_tolerance(
            visual_error
        ):

            print(
                "目标已进入控制容差范围"
            )

            return True

        # 🔴【确认还需要控制，再更新PID】
        control = (
            self.calculate_control(
                visual_error
            )
        )

        # 🔴【新增】
        print(
            "PID控制输出：",
            (
                round(control[0], 2),
                round(control[1], 2)
            )
        )
        print(
            "目标像素位置：",
            detection_result.center
        )

        return True