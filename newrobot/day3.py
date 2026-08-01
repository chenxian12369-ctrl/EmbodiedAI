print("====================")
print("机器人巡检系统启动")
print("====================")

battery = 100
areas = [
    "A区域",
    "B区域",
    "C区域",
    "D区域",
    "E区域"
]


for area in areas:
    battery -= 10
    print()

    print("正在巡检：", area)

    command = input("输入状态(normal/warning): ")

    if command == "warning":

        print("发现异常！")

        print("机器人停止巡检")

        break
    if battery < 80:
        
        print("电量不足，请立即返回充电")

        break

    else:

        print("区域正常")


print()

print("巡检任务结束")