from robot import Robot


class RobotManager:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def show_all(self):
        print()
        print("机器人列表")
        print("----------------")

        for robot in self.robots:
            robot.status()
            print("----------------")

    def find_robot(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot

        return None
    def remove_robot(self, name):

        for robot in self.robots:

            if robot.name == name:

                self.robots.remove(robot)

                print(name, "已删除")

                return

        print("机器人不存在")
    def move_all(self, direction):

        for robot in self.robots:

            robot.move(direction)
    def robot_count(self):

        print("机器人数量：", len(self.robots))
    def check_all_battery(self):

        for robot in self.robots:

            if robot.battery <= 20:

                print(robot.name, "需要充电")
    def check_all_battery(self):

        for robot in self.robots:

            if robot.battery <= 20:

                print(robot.name, "需要充电")
    def charge_all(self):
        for robot in self.robots:
            robot.charge()