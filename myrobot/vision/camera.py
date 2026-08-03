import cv2


class Camera:


    def capture(self,path):

        image=cv2.imread(path)

        return image