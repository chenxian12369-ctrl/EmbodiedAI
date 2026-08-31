import cv2


class VideoFrameSource:

    def __init__(self, video_path):

        self.video_path = video_path

        self.capture = cv2.VideoCapture(
            video_path
        )

        self.frame_number = 0


    def get_next_frame(self):

        success, image = self.capture.read()

        if not success:
            return None, True, None, None

        self.frame_number += 1

        return (
            image,
            False,
            self.frame_number,
            None
        )


    def release(self):

        self.capture.release()