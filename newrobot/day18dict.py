robot = {
    "name": "A01",
    "battery": 70,
    "location": "FAB1"
}
robot["battery"] = 100
print(robot)

def to_dict(self):
    """
    将机器人对象转换成字典
    """
    return {

        "name": self.name,

        "battery": self.battery,

        "location": self.location

    }
robot1 = robot("A01",70,"FAB1")

print(robot1.to_dict())