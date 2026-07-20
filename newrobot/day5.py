print("====================")
print("机器人控制系统")
print("====================")


def start():

    print("机器人启动")


def move(direction, speed):

    print(
        "移动方向:",
        direction,
        "速度:",
        speed
    )


def scan(area):

    print(
        "正在扫描区域:",
        area
    )


def charge():

    print("机器人正在充电")


def get_battery():

    battery = 75

    return battery

def check_obstacle(distance):
    if distance < 1:

        return True

    else:

        return False

# 主程序

start()


move(
    "前方",
    1.5
)


scan(
    "FAB1设备区"
)


power = get_battery()


print(
    "当前电量:",
    power
)
#
result = check_obstacle(2)
if result == True:
    print("停止")
else:
    print("go on")
#
    if power < 20:

        charge()
        print(
            "电量正常，继工作"
        )

    else:

        print(
            "电量正常，继续工作"
        )