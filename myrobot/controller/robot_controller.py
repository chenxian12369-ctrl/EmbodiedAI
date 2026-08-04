class RobotController:

    def move_to_target(
        self,
        detection_result
    ):

        if not detection_result.is_valid(500):

            print(
                "目标太小，忽略"
            )

            return

        print(
            "机器人准备移动"
        )

        print(
            "移动目标：",
            detection_result.center
        )