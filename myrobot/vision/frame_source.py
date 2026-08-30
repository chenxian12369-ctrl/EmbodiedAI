class ImageFrameSource:

    def __init__(self, camera, image_paths):
        self.camera = camera
        self.image_paths = image_paths
        self.current_index = 0

    def get_next_frame(self):

        if self.current_index >= len(self.image_paths):
       
            return None, True, None, None

        frame_number = self.current_index + 1

        image_path = self.image_paths[
            self.current_index
        ]

        self.current_index += 1

        try:
            image = self.camera.capture(
                image_path
            )

        except (
    FileNotFoundError,
    ValueError
        ) as error:

    # 🔴【修改】不在这里打印，只把错误返回给 main
            return None, False, frame_number, error

        return image, False, frame_number, None