class GripperService:


    def __init__(self,robot):

        self.robot = robot



    def handle_request(self,command):


        if command == "open":

            result = self.robot.open_gripper()


        elif command == "close":

            result = self.robot.close_gripper()


        else:

            print("未知命令")

            result = False



        return result