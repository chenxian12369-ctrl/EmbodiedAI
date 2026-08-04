class RobotController:

    def move_to_target(
        self,
        detection_result
    ):
        """
        根据检测结果移动机器人
        """

        print(
            "机器人准备移动"
        )

        print(
            "目标中心：",
            detection_result.center
        )