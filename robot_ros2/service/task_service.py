class TaskService:


    def __init__(self,action):

        self.action=action



    def request_move(self,target):

        print(
            "收到移动请求"
        )


        result=self.action.execute(target)


        return result