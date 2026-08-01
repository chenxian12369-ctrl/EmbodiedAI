from robot import Robot
from service import GripperService



robot = Robot("Arm01")


service = GripperService(robot)



result = service.handle_request(
    "open"
)


print(
    "执行结果:",
    result
)



result = service.handle_request(
    "close"
)


print(
    "执行结果:",
    result
)