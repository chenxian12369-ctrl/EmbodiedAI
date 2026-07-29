from robot.transport_robot import TransportRobot
from robot.inspect_robot import InspectRobot
from robot.cleaning_robot import CleaningRobot
from robot.security_robot import SecurityRobot
from robot.delivery_robot import DeliveryRobot

class RobotFactory:
    """
    根据配置数据创建不同类型的机器人对象。
    """

    ROBOT_MAP = {
        "TransportRobot": TransportRobot,
        "InspectRobot": InspectRobot,
        "CleaningRobot": CleaningRobot,
        "SecurityRobot": SecurityRobot,
        "DeliveryRobot": DeliveryRobot
    }

    @staticmethod
    def create_robot(data):
        """
        根据配置中的机器人类型、名称和电量创建机器人对象。
        """
        robot_type = data["type"]

        robot_class = RobotFactory.ROBOT_MAP.get(robot_type)

        if robot_class is None:
            raise ValueError(f"未知机器人类型：{robot_type}")

        return robot_class(
            data["name"],
            data["battery"]
        )