class RobotController:

  

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


        print(
            "移动到：",
            detection_result.center
        )

        return True