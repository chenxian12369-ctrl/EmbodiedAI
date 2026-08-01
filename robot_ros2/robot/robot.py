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
    def move(self,target):

        print("开始移动到",target)

        for i in [20,50,80,100]:

            print("进度:",i,"%")

        print("移动完成")

        return True

