class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def status(self):
        print("机器人：", self.name)
        print("电量：", self.battery)

    def charge(self):
        self.battery = 100
        print(self.name, "充电完成")

    def move(self, direction):
        if self.battery <= 0:
            print(self.name, "没有电")
            return

        print(self.name, "移动方向：", direction)
        self.battery -= 10

    def work(self):
        print(self.name, "开始工作")

    def repair(self):
        if self.battery == 0:
            print(self.name, "机器人维修完成")
        else:
            print(self.name, "机器人正常")