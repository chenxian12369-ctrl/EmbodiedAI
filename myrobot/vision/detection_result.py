class DetectionResult:


    def __init__(
        self,
        area,
        center,
        bounding_box
    ):

        self.area = area

        self.center = center

        self.bounding_box = bounding_box



    def is_valid(self, min_area=100):

        return self.area >= min_area



    def get_width(self):

        return self.bounding_box[2]



    def get_height(self):

        return self.bounding_box[3]



    def show(self):

        print(
            "目标面积:",
            self.area
        )

        print(
            "目标中心:",
            self.center
        )

        print(
            "目标尺寸:",
            self.bounding_box
        )



    def get_image_position(self):
        """
        返回图像坐标
        """

        return self.center