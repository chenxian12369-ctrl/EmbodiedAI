class MoveAction:


    def __init__(self,robot):

        self.robot=robot



    def execute(self,target):

        print("开始执行移动任务")


        result=self.robot.move(target)


        if result:

            print("任务完成")


        else:

            print("任务失败")


        return result