from robot import Robot


class RobotManager:


    def __init__(self):

        self.robots = []



    def add_robot(self,robot):

        self.robots.append(robot)



    def show_all(self):

        print()

        print("机器人列表")

        print("--------------")



        for robot in self.robots:

            robot.status()