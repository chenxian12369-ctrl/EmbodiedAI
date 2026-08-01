class MoveAction:


    def __init__(self,robot):

        self.robot=robot


    def execute(self,target):

        result=self.robot.move(target)

        return result