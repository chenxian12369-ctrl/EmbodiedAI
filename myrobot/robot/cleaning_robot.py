from robot.robot import Robot

# 清洁机器人
class CleaningRobot(Robot):

    def work(self):
        print(self.name, "正在清洁地面")