from robot import Robot

from robot_manager import RobotManager



manager = RobotManager()



robot1 = Robot(
    "Robot_A01",
    80
)

robot2 = Robot(
    "Robot_A02",
    60
)



manager.add_robot(robot1)

manager.add_robot(robot2)



manager.show_all()