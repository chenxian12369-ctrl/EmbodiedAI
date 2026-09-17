class RobotController:
    def __init__(
    self,
    image_width=640,
    image_height=480,
    kp=0.1,
    control_tolerance=5
):

        self.image_center = (
            image_width // 2,
            image_height // 2
        )

        self.kp = kp

        # 🔴【新增】
        self.control_tolerance = (
            control_tolerance
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
            self.kp * error_x
        )

        control_y = (
            self.kp * error_y
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
        control = (
    self.calculate_control(
        visual_error
    )
)
        if self.is_error_within_tolerance(
    visual_error
):

            print(
                "目标已进入控制容差范围"
            )

            return True

        # 🔴【新增】
        print(
            "P控制输出：",
            control
        )

        print(
            "移动到：",
            detection_result.center
        )

        return True