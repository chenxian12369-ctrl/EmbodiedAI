import json


class Camera:


    def __init__(self,config):

        self.fps=config["fps"]

        self.resolution=config["resolution"]



    def show(self):

        print(
            "fps:",
            self.fps
        )

        print(
            "分辨率:",
            self.resolution
        )