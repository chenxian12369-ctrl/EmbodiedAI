print("=====机器人信息录入=====")

name = input("机器人名字：")

robot_type = input("机器人类型：")

battery = int(input("当前电量："))

print()

print("机器人信息")

print("名字：", name)

print("类型：", robot_type)

print("电量：", battery)

if battery >= 80:
    print("状态：可以执行复杂任务")

elif battery >= 50:
    print("状态：可以正常工作")

elif battery >= 20:
    print("状态：建议充电")

else:
    print("状态：立即返回充电")