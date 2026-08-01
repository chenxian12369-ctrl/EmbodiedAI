# day46from robot.robot import Robot
# from action.move_action import MoveAction
# from service.task_service import TaskService


# robot=Robot(
#     "A01",
#     100
# )


# action=MoveAction(robot)


# service=TaskService(action)



# result=service.request_move(
#     "FAB1"
# )


# print(result)


# print(robot.status())

from topic import Topic
from camera import Camera
from detector import Detector



image_topic = Topic()



camera = Camera(
    image_topic
)


detector = Detector()



image_topic.subscribe(
    detector.detect
)



camera.capture()