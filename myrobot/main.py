from robot.transport_robot import TransportRobot
from robot.inspect_robot import InspectRobot
from robot.cleaning_robot import CleaningRobot
from robot.security_robot import SecurityRobot

from manager.robot_manager import RobotManager
from config.settings import DEFAULT_DIRECTION
from config.settings import SYSTEM_NAME
from utils.logger import write_log
print("=" * 30)
print(SYSTEM_NAME)
print("=" * 30)

write_log(
    "==========系统启动=========="
)

def start_system():

    manager = RobotManager()

    robot1 = TransportRobot("A01", 70)
    robot2 = InspectRobot("A02", 5)
    robot3 = CleaningRobot("A03", 50)
    robot4 = SecurityRobot("A04", 80)

    manager.add_robot(robot1)
    manager.add_robot(robot2)
    manager.add_robot(robot3)
    manager.add_robot(robot4)

    manager.robot_count()
    manager.show_all()
    manager.check_all_battery()
    manager.work_all()
    manager.move_all(DEFAULT_DIRECTION)


if __name__ == "__main__":
    start_system()