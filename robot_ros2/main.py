from robot import Robot
from robot_ros2.service.service import GripperService
from action import MoveAction


robot=Robot("A")


action=MoveAction(robot)


result=action.execute(
    (10,20,30)
)


print("结果:",result)


# robot = Robot("Arm01")


# service = GripperService(robot)



# result = service.handle_request(
#     "open"
# )


# print(
#     "执行结果:",
#     result
# )



# result = service.handle_request(
#     "close"
# )


# print(
#     "执行结果:",
#     result
# )