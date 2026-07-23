from robot import Robot
from robot import TransportRobot
from robot import CleaningRobot
from robot import InspectRobot
from robot_manager import RobotManager



manager = RobotManager()

robot1 = TransportRobot("搬运",80)

robot2 = InspectRobot("巡检",60)
robot3 = CleaningRobot("巡检",60)

robot1.status()

robot1.move_box()

robot2.status()

robot2.inspect()

robot3.status()

robot3.charge()

robot3.clean()
'''
robot1 = Robot("Robot_A01",80)

robot2 = Robot("Robot_A02",15)

robot3 = Robot("Robot_A03",60)

manager.add_robot(robot1)

manager.add_robot(robot2)

manager.add_robot(robot3)





manager.show_all()


search_name = input("请输入要查找的机器人名称：")

result = manager.find_robot(search_name)

if result is not None:
    print("找到机器人：")
    result.status()
else:
    print("未找到机器人")
    '''
'''
manager.robot_count()

manager.show_all()

manager.check_all_battery()

manager.move_all("前方")

manager.remove_robot("Robot_A02")

manager.robot_count()
manager.charge_all()


manager.show_all()
'''