import cv2


class DVideoProc:

    def __init__(self):
        self.__activate = False

    @property
    def activate(self):
        return self.__activate

    @activate.setter
    def activate(self, activate):
        self.__activate = activate

    def process(self, frame):
        raise Exception("DVideoProc is an Abstract Interface")


class DVideoProcFreeze(DVideoProc):

    def __init__(self):
        super().__init__()
        self.__frame = None

    def __str__(self):
        return "Freeze Video Processor"

    def process(self, frame):
        if not self.activate:
            self.__frame = frame

        return self.__frame


class DVideoProcGrayscale(DVideoProc):

    def __str__(self):
        return "Grayscale Video Processor"

    def process(self, frame):
        if not self.activate:
            return frame

        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
