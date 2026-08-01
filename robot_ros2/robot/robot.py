from utils.logger import write_log


class Robot:


    def __init__(self,name,battery):

        self.name=name
        self.battery=battery


    def move(self,target):

        print(
            self.name,
            "移动到",
            target
        )

        write_log(
            f"{self.name}移动到{target}"
        )


        self.battery -= 10


        return True



    def status(self):

        return {
            "name":self.name,
            "battery":self.battery
        }