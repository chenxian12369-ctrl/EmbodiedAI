class Topic:


    def __init__(self):

        self.subscribers = []


    def subscribe(self,callback):

        self.subscribers.append(callback)



    def publish(self,message):

        for subscriber in self.subscribers:

            subscriber(message)