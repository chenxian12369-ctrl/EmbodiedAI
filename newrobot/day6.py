print("====================")
print("机器人对象系统")
print("====================")


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
def menu():

    print()

    print("======Robot Console======")

    print("1. 查看状态")

    print("2. 移动机器人")

    print("3. 充电")

    print("4. 修改位置")

    print("5. 退出")
# 创建机器人


robot1 = Robot(
    "Robot_A01",
    80
)


robot2 = Robot(
    "Robot_A02",
    60
)



robot1.start()

robot1.move("前方")

robot1.status()



print()

robot1.change_battery(50)

robot2.change_battery(90)

robot1.status()

robot2.status()

robot2.start()

robot2.move("右侧")

robot2.status()

robot1.change_location("FAB2")