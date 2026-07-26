from robot.robot import Robot


class InspectRobot(Robot):

    def work(self):
        print(self.name, "开始巡检设备")