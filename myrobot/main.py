from robot.transport_robot import TransportRobot
from robot.inspect_robot import InspectRobot
from robot.cleaning_robot import CleaningRobot
from robot.security_robot import SecurityRobot
from robot.robot import Robot
from manager.robot_manager import RobotManager
from config.settings import DEFAULT_DIRECTION
from config.settings import SYSTEM_NAME
from utils.logger import write_log
from robot.robot_factory import RobotFactory
from utils.config_loader import load_config
print("=" * 30)
print(SYSTEM_NAME)
print("=" * 30)

write_log(
    "==========系统启动=========="
)

def start_system():

    manager = RobotManager()

    robots_config = load_config(
        "config/robots_config.json"
    )   

    for data in robots_config:

        robot = RobotFactory.create_robot(data)

        manager.add_robot(robot)
    # robot1.start()
    manager.work_all()
    # day21代码
    # manager.remove_robot("A04")
    # manager.robot_count()
    # manager.show_all()
    # manager.check_all_battery()
    # manager.move_all(DEFAULT_DIRECTION)
    # manager.charge_all()
    # manager.load_all()
    # manager.save_all()
    # robots_data = manager.load_data()

    # print(robots_data)

    manager.load_all()

    manager.show_all()
    


if __name__ == "__main__":
    start_system()
    # day17代码
    # Robot.system_author()

    # Robot.system_name()

    # Robot.show_version()
    # print(Robot.check_battery(80))

    # print(Robot.check_battery(150))

    # print(Robot.check_battery(-5))

    # Robot.battery_level(90)

    # Robot.battery_level(40)

    # Robot.battery_level(10)
    # day18代码
    # robot1 = Robot("A01", 70)
    # print(robot1.to_dict())
    
