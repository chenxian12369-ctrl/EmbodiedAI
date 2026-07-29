from robot.robot import Robot


class MedicalRobot(Robot):
    """
    医疗机器人。
    """

    def work(self):
        """
        执行医疗任务。
        """
        print(self.name, "正在执行医疗任务")