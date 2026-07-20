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

    print("6. 查看任务列表")
# 创建机器人

tasks = [
"巡检",
"搬运",
"充电"
]
robot1 = Robot(
    "Robot_A01",
    80
)


robot2 = Robot(
    "Robot_A02",
    60
)


menu()

while True:
    choice = input("请输入:")
    if choice == "1":

     robot1.status()
    elif choice == "2":

       direction = input("请输入方向:")

       robot1.move(direction)

    elif choice == "3":

      robot1.charge()
    
    elif choice == "4":

      new_location = input("输入新位置:")

      robot1.change_location(new_location)
    elif choice == "5":
        break
    elif choice == "6":
        print("任务列表：")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
  
       
    else:
        print("无效输入")
