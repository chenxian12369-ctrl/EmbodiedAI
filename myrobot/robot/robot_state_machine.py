from robot.robot_state import RobotState


class RobotStateMachine:

    def __init__(self):

        # 🔴【新增】机器人初始状态
        self.state = RobotState.SEARCHING

    def get_state(self):
        return self.state
    def is_stable(self):
        return self.state == RobotState.STABLE

    def target_found(self):

        if self.state == RobotState.SEARCHING:
            self.state = RobotState.TRACKING

    def target_stable(self):

        if self.state == RobotState.TRACKING:
            self.state = RobotState.STABLE

    def start_moving(self):

        if self.state == RobotState.STABLE:
            self.state = RobotState.MOVING

    def target_lost(self):

        self.state = RobotState.SEARCHING