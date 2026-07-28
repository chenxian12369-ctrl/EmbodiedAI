from config.settings import LOW_BATTERY_LEVEL
from utils.logger import write_log

class RobotManager:

    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)
        write_log(
        f"{robot.name} 已加入系统"
        )

    def remove_robot(self, name):
        for robot in self.robots:
            if robot.name == name:
                self.robots.remove(robot)
                print(name, "已删除")
            write_log(
            f"{name} 已删除"
            )
            return

        print("机器人不存在")

    def find_robot(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot

        return None

    def robot_count(self):
        print("机器人数量：", len(self.robots))

    def show_all(self):
        print()
        print("机器人列表")
        print("----------------")

        for robot in self.robots:
            robot.status()
            print(robot.__class__.__name__)
            print("----------------")

    def work_all(self):
        for robot in self.robots:
            robot.work()

    def move_all(self, direction):
        for robot in self.robots:
            robot.move(direction)

    def charge_all(self):
        for robot in self.robots:
            robot.charge()

    def check_all_battery(self):
        for robot in self.robots:
            if robot.battery <= LOW_BATTERY_LEVEL:
                print(robot.name, "需要充电")