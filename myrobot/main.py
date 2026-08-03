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
from utils.config_loader import ConfigLoader
from config.config_loader import ConfigLoader
import cv2

print(cv2.__version__)

from vision.camera import Camera
from vision.image_processor import ImageProcessor

from vision.camera import Camera
from vision.image_processor import ImageProcessor


def test_vision():

    camera = Camera()

    image = camera.capture(
        "images/test.jpg"
    )

    resized_image = ImageProcessor.resize(
        image,
        640,
        480
    )

    gray_image = ImageProcessor.to_gray(
        resized_image
    )

    binary_image = ImageProcessor.threshold(
        gray_image,
        127
    )

    edge_image = ImageProcessor.detect_edges(
        gray_image,
        100,
        200
    )
    binary_50 = ImageProcessor.threshold(
    gray_image,
    50
    )

    binary_200 = ImageProcessor.threshold(
        gray_image,
        200
    )
    ImageProcessor.save(
        binary_50,
        "images/output/binary_50.jpg"
    )

    ImageProcessor.save(
        binary_200,
        "images/output/binary_200.jpg"
    )

    print(
        "原始图形状：",
        image.shape
    )

    print(
        "灰度图形状：",
        gray_image.shape
    )

    print(
        "二值图形状：",
        binary_image.shape
    )

    print(
        "边缘图形状：",
        edge_image.shape
    )

    ImageProcessor.save(
        binary_image,
        "images/output/binary.jpg"
    )

    ImageProcessor.save(
        edge_image,
        "images/output/edges.jpg"
    )


test_vision()

# day49
# camera=Camera()


# image=camera.capture(
#     "test.jpg"
# )


# print(type(image))

# print(image.shape)


# print("=" * 30)
# print(SYSTEM_NAME)
# print("=" * 30)

write_log(
    "==========系统启动=========="
)

def start_system():




    # config = ConfigLoader.load()

    # print(config)
    print("over" )

    # manager = RobotManager()

    # config = ConfigLoader.load()

    # for data in robots_config:

    #     robot = RobotFactory.create_robot(data)

    #     manager.add_robot(robot)
    # robot1.start()
    # manager.work_all()
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
    
    # manager.load_all()

    # manager.show_all()
    


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
    
    # robot = Robot("A01", 70)

    # print(robot.battery)

    # robot.battery = 30

    # print(robot.battery)

    # robot.battery = 300