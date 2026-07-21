
'''file = open("robot_log.txt","w")

file.write("Robot Start\n")

file.write("Battery:80\n")

file.write("Location:FAB1\n")

file.close()

print("日志保存成功")

file = open("robot_log.txt","r")

content = file.read()

print(content)

file.close()'''
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
    def save_robot(robot):
        try:
            with open("robot.txt", "w", encoding="utf-8") as file:
                file.write(robot.name + "\n")
                file.write(str(robot.battery) + "\n")
                file.write(robot.location + "\n")
            print("保存成功")
        except Exception as e:
            print("保存失败：", e)
    @staticmethod
    def load_robot():

        file = open("robot.txt","r")

        lines = file.readlines()

        file.close()

        robot = Robot(

            lines[0].strip(),

            int(lines[1])

        )

        robot.location = lines[2].strip()

        return robot


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

    print("7.保存机器人")
    print("8.加载机器人")
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
    
    elif choice == "7":
        robot1.change_location("FAB8")
        robot1.save_robot()
        

    elif choice == "8":
        robot1=Robot.load_robot()

        print("读取成功")
    else:
        print("无效输入")
