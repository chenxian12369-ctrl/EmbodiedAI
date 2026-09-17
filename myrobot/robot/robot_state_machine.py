from robot.robot_state import RobotState


class RobotStateMachine:

    def __init__(
        self,
        required_lost_frames=3
    ):
        self.state = RobotState.SEARCHING

        # 🔴【新增】连续丢失次数
        self.lost_count = 0

        # 🔴【新增】确认目标丢失所需帧数
        self.required_lost_frames = (
            required_lost_frames
        )

    def get_state(self):
        return self.state
    def is_stable(self):
        return self.state == RobotState.STABLE
    def _transition_to(self, new_state):

        old_state = self.state

        self.state = new_state

        print(
            "状态转换：",
            old_state.value,
            "->",
            new_state.value
    )

    def target_found(self):
        self.lost_count = 0
        if self.state == RobotState.SEARCHING:

            # 🔴【修改】
            self._transition_to(
                RobotState.TRACKING
        )

    def target_stable(self):

        if self.state == RobotState.TRACKING:

            # 🔴【修改】
            self._transition_to(
                RobotState.STABLE
            )
    def start_moving(self):

        if self.state == RobotState.STABLE:

            # 🔴【修改】
            self._transition_to(
                RobotState.MOVING
            )
        else:

            print(
                "非法状态转换：",
                self.state.value,
                "不能直接进入 moving"
            )
    def is_error(self):
        return self.state == RobotState.ERROR


    def recover(self):

        if self.state == RobotState.ERROR:

            self._transition_to(
                RobotState.SEARCHING
            )
    def target_lost(self):

        if self.state == RobotState.SEARCHING:
            return False

        self.lost_count += 1

        print(
            "连续丢失次数：",
            self.lost_count
        )

        if (
            self.lost_count
            < self.required_lost_frames
        ):
            return False

        if self.state == RobotState.MOVING:

            self._transition_to(
                RobotState.ERROR
            )

        else:

            self._transition_to(
                RobotState.SEARCHING
            )

        self.lost_count = 0

        return True