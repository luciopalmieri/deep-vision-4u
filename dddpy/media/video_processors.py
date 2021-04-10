import cv2


class DVideoProc:

    @staticmethod
    def process(frame):
        raise Exception("DVideoProc is an Abstract Interface")


class DVideoProcGrayscale(DVideoProc):

    @staticmethod
    def process(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def __str__(self):
        return "Grayscale Video Processor"
