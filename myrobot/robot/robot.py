from utils.logger import write_log

class Robot:
    @staticmethod
    def show_version():

        print("Robot System v1.0")
    @staticmethod
    @staticmethod
    def system_author():

        print("Author: Chen Xian")
    @staticmethod
    def system_name():

        print("Semiconductor Robot System")
    @staticmethod
    def check_battery(value):

        if value < 0:

            return False

        if value > 100:

            return False

        return True
    @staticmethod
    def battery_level(level):

        if level >= 80:

            print("高电量")

        elif level >= 30:

            print("中电量")

        else:

            print("低电量")
    @classmethod
    def from_dict(cls, data):
        """
        根据字典创建Robot对象
        """

        return cls(
            data["name"],
            data["battery"]
        )
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
    def start(self):

        print(self.name,"启动")

        write_log(
        f"{self.name} 启动"
        )
    
    def status(self):
        print("机器人：", self.name)
        print("电量：", self.battery)
    def to_dict(self):
        return {
            "name": self.name,
            "battery": self.battery,
     
        }
    @classmethod
    def from_dict(cls, data):
        """
        根据字典创建机器人对象
        """
        robot = cls(
            data["name"],
            data["battery"]
        )


        return robot
    def charge(self):

        self.battery = 100

        print(self.name,"充电完成")

        write_log(f"{self.name} 完成充电")

    def move(self, direction):
        
        if self.battery <= 20:
            write_log(f"{self.name} 电量不足，移动失败")
            print(self.name, "没有电")
            return

        print(self.name, "移动方向：", direction)
        write_log(
        f"{self.name} 向 {direction} 移动"
        )
        self.battery -= 10
    """
    子类必须重写此方法
    """
    def work(self):
        pass

    def repair(self):
        if self.battery == 0:
            print(self.name, "机器人维修完成")
        else:
            print(self.name, "机器人正常")