class Robot:


    def __init__(self,name,battery):

        self.name = name

        self.battery = battery

        self.location="FAB1"

        self.battery -=10



    def start(self):

        print(
            self.name,
            "启动"
        )



    def move(self,direction):
        self.battery -=10
        print(
            self.name,
            "移动方向:",
            direction
        )



    def charge(self):

        self.battery = 100

        print(
            self.name,
            "充电完成"
        )



    def status(self):

        print(
            "机器人:",
            self.name
        )

        print(
            "电量:",
            self.battery
        )

    def change_battery(self, value):
        self.battery = value
    def change_location(self,new_location):

        self.location=new_location
class TransportRobot(Robot):
    def move_box(self):

        print(self.name, "正在搬运晶圆")
class CleaningRobot(Robot):
    def clean(self):

        print(self.name, "正在清洁地面")
class InspectRobot(Robot):

    def inspect(self):

        print(self.name, "开始巡检")