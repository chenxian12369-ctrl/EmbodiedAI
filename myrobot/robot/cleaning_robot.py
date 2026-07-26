from robot.robot import Robot


class CleaningRobot(Robot):

    def work(self):
        print(self.name, "正在清洁地面")