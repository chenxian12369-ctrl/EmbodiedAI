class Camera:


    def __init__(self,topic):

        self.topic = topic



    def capture(self):

        image="wafer_image_001"


        print(
            "Camera发布图片"
        )


        self.topic.publish(image)