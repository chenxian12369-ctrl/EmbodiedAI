from config.settings import LOW_BATTERY_LEVEL
from utils.logger import write_log
from config.settings import DATA_FILE
import json
from robot.robot import Robot


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
    def save_all(self):
    # """
    # 将所有机器人信息保存到JSON文件。
    # """
        robots_data = []

        for robot in self.robots:
            robots_data.append(robot.to_dict())

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(
                robots_data,
                file,
                ensure_ascii=False,
                indent=4
            )
    def load_all(self):
        """
        从JSON文件读取机器人数据
        """

        try:

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                robots_data = json.load(file)


        except FileNotFoundError:

            print("机器人数据文件不存在")
            write_log(
            "读取失败：机器人数据文件不存在"
            )

            return


        except json.JSONDecodeError:

            print("JSON格式错误")
            write_log(
            "JSON格式错误"
            )


            return


        print("机器人数据读取成功")

    def load_data(self):
        """
        从JSON文件读取机器人字典数据。
        """
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                robots_data = json.load(file)

            return robots_data

        except FileNotFoundError:
            print("机器人数据文件不存在")
            return []


    print("机器人数据保存成功")

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