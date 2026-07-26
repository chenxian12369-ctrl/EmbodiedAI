from robot.robot import Robot


class TransportRobot(Robot):

    def work(self):
        print(self.name, "正在搬运晶圆")