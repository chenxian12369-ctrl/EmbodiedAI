import cv2


class Camera:


    def capture(self,path):

        image=cv2.imread(path)
        if image is None:
            raise FileNotFoundError(
                f"无法读取图片：{path}"
            )

        return image

        return image