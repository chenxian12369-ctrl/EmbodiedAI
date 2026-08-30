class ImageFrameSource:

    def __init__(
        self,
        camera,
        image_paths
    ):

        self.camera = camera
        self.image_paths = image_paths

        self.current_index = 0


    def get_next_frame(self):

        # 所有图片已经读取完
        if (
            self.current_index
            >=
            len(self.image_paths)
        ):

            return None


        # 获取当前图片路径
        image_path = self.image_paths[
            self.current_index
        ]


        # 下标向后移动
        self.current_index += 1


        # 读取图片
        image = self.camera.capture(
            image_path
        )


        return image