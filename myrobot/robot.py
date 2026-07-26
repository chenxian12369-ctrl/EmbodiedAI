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
    def repair(self):
        if self.battery <= 0:

            print(self.name, "机器人维修完成")

            return
        else:
            print(self.name, "机器人正常")


    def move(self,direction):
        if self.battery <= 0:

            print(self.name, "没有电")

            return

        print(self.name, "移动方向：", direction)

        self.battery -= 10



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
    def work(self):
        print(self.name, "正在搬运晶圆")
class InspectRobot(Robot):

    def inspect(self):

        print(self.name, "开始巡检")
    def work(self):
        print(self.name, "开始巡检设备")
class CleaningRobot(Robot):
    def clean(self):

        print(self.name, "正在清洁地面")
    def work(self):
        print(self.name, "正在清洁地面")
class SecurityRobot(Robot):
    
    
    def work(self):
        print(self.name, "正在夜间巡逻")