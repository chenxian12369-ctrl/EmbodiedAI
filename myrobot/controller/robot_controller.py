class RobotController:

    # def move_to_target(
    #     self,
    #     detection_result
    # ):

    #     if not detection_result.is_valid(500):

    #         print(
    #             "目标太小，忽略"
    #         )

    #         return

    #     print(
    #         "机器人准备移动"
    #     )

    #     print(
    #         "移动目标：",
    #         detection_result.center
    #     )

    def move_to_target(
        self,
        robot,
        detection_result
    ):

        if robot.state != "idle":
            print(
                "机器人当前忙碌，拒绝新任务"
            )

            return False

        if not detection_result.is_valid(500):
            print(
                "目标太小，忽略"
            )

            return False

        robot.change_state(
            "moving"
        )

        print(
            "移动到：",
            detection_result.center
        )

        return True