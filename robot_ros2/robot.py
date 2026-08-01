class Robot:


    def __init__(self,name):

        self.name = name
        self.gripper = False



    def open_gripper(self):

        self.gripper = True

        print(
            self.name,
            "夹爪打开"
        )

        return True



    def close_gripper(self):

        self.gripper = False

        print(
            self.name,
            "夹爪关闭"
        )

        return True