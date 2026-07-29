from robot.robot import Robot


class DeliveryRobot(Robot):
    """
    配送机器人。
    """

    def work(self):
        """
        执行物料配送任务。
        """
        print(self.name, "正在配送物料")