class RobotController:
    def __init__(
        self,
        image_width=640,
        image_height=480
    ):

        self.image_center = (
            image_width // 2,
            image_height // 2
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

        print(
            "移动到：",
            detection_result.center
        )

        return True