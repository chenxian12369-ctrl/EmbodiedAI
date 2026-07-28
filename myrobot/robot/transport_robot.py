from robot.robot import Robot
from utils.logger import write_log

class TransportRobot(Robot):

    def work(self):
        print(self.name, "正在搬运晶圆")
        write_log(f"{self.name} 正在搬运晶圆")