print("===================")
print("机器人状态管理系统")
print("===================")


robot = {
    "name": "Robot_A01",
    "battery": 100,
    "location": "FAB1",
    "task": "巡检"
}


tasks = [
    "检查设备",
    "采集数据",
    "返回基地"
]


print("\n机器人信息:")

for key,value in robot.items():
    print(key, ":", value)



print("\n任务列表:")

for task in tasks:
    print("-", task)



print("\n机器人开始执行任务")


for task in tasks:

    print("执行:", task)

    robot["battery"] -= 20


    print("当前电量:",
          robot["battery"])


    if robot["battery"] <= 20:

        print("电量不足，返回充电")

        robot["task"] = "充电"

        break



print("\n最终状态:")

for key,value in robot.items():

    print(key,":",value)