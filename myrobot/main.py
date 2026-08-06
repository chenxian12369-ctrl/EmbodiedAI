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
from controller.robot_controller import RobotController
print(cv2.__version__)
from planner.task_planner import TaskPlanner
from vision.camera import Camera
from vision.image_processor import ImageProcessor

from vision.camera import Camera
from vision.image_processor import ImageProcessor
from vision.detector import Detector
from vision.camera import Camera
from vision.detector import Detector
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
            220
        )
    contours = Detector.find_contours(

        binary_image

    )


    print(

        "轮廓数量：",

        len(contours)

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
    contour_image = ImageProcessor.draw_contours(

    resized_image,

    contours

)

    ImageProcessor.save(

        contour_image,

        "images/output/contours.jpg"

    )
     # 先复制原图，后面在副本上持续画图
    result_image = resized_image.copy()

    # 6. 绘制所有轮廓
    result_image = ImageProcessor.draw_contours(
        result_image,
        contours
    )

    # 7. 依次计算每个轮廓的中心
    for index, contour in enumerate(
        contours,
        start=1
    ):

        center = Detector.find_center(
            contour
        )

        if center is None:
            print(
                f"轮廓{index}无法计算中心"
            )

            continue

        print(
            f"轮廓{index}中心坐标：",
            center
        )

        result_image = ImageProcessor.draw_center(
            result_image,
            center
        )

    # 8. 保存最终结果
    ImageProcessor.save(
        result_image,
        "images/output/centers.jpg"
    )
    print("轮廓总数：", len(contours))
# reason for can not count
    for index, contour in enumerate(contours[:20], start=1):
        area = cv2.contourArea(contour)
        moments = cv2.moments(contour)

        print(
            f"轮廓{index}：",
            "点数 =", len(contour),
            "面积 =", area,
            "m00 =", moments["m00"]
        )
    print(
    "传入轮廓检测的图片形状：",
    binary_image.shape
)
    ImageProcessor.save(
    binary_image,
    "images/output/debug_binary.jpg"
)
    # day54
#     valid_contours = Detector.filter_contours(
#     contours,
#     min_area=100
# )

#     print(
#         "有效轮廓数量：",
#         len(valid_contours)
#     )

#     result_image = resized_image.copy()

#     for index, contour in enumerate(
#         valid_contours,
#         start=1
#     ):

#         target_info = Detector.analyze_contour(
#             contour
#         )

#         print(
#             f"目标{index}信息：",
#             target_info
#         )

#         center = target_info["center"]
#         bounding_box = target_info["bounding_box"]

#         if center is not None:

#             result_image = ImageProcessor.draw_center(
#                 result_image,
#                 center
#             )

#         result_image = ImageProcessor.draw_bounding_box(
#             result_image,
#             bounding_box
#         )

#     ImageProcessor.save(
#         result_image,
#         "images/output/targets.jpg"
#     )
    # 获取轮廓

    contours = Detector.find_contours(
        binary_image
    )


    # 过滤

    valid_contours = Detector.filter_contours(
        contours,
        min_area=100
    )


    # 保存检测结果

    results=[]


    for contour in valid_contours:


        result = Detector.analyze_contour(
            contour
        )


        results.append(result)


        result.show()



    # 找最大目标
    robot = Robot("A01", 80)
    planner = TaskPlanner()

    controller = RobotController()

    selected_target = planner.select_target(
            results
        )

    if selected_target is not None:

        move_result = controller.move_to_target(
                        robot,
                        selected_target
                    )
        
        print(
                        "移动请求结果：",
                        move_result
                    )
        
    
        # largest_target.show()



    # 绘制结果

    result_image=resized_image.copy()


    for result in results:


        result_image=ImageProcessor.draw_center(

            result_image,

            result.center

        )


        result_image=ImageProcessor.draw_bounding_box(

            result_image,

            result.bounding_box

        )
    for result in results:

        print(
            "图像坐标:",
            result.get_image_position()
        )


    # controller.move_to_target(

    #     robot,

    #     largest_target

    # )
    ImageProcessor.save(

        result_image,

        "images/output/targets.jpg"

    )
    
#day60    move_result = controller.move_to_target(
#     robot,
#     largest_target
# )

#     print(
#         "移动请求结果：",
#         move_result
#     )
#     second_result = controller.move_to_target(
#     robot,
#     largest_target
# )

#     print(
#         "第二次移动请求结果：",
#         second_result
#     )
#     robot.finish_task()

#     third_result = controller.move_to_target(
#         robot,
#         largest_target
#     )

#     print(
#         "第三次移动请求结果：",
#         third_result
#     )



test_vision()

# day49
# camera=Camera()


# image=camera.capture(
#     "test.jpg"
# )


# print(type(image))

# print(image.shape)


# print("=" * 30)# 保存检测结果


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