import cv2
from datetime import datetime


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

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        return frame


class DVideoProcDateTime(DVideoProc):

    def __init__(self, date_time_fmt="%d %b %Y, %H:%M:%S"):
        super().__init__()
        self.__date_time_fmt = date_time_fmt

    def __str__(self):
        return "Date/Time Video Processor"

    def process(self, frame):
        if not self.activate:
            return frame

        now = datetime.now()
        str_now = now.strftime(self.__date_time_fmt)
        cv2.putText(frame, str_now, (20, frame.shape[0] - 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)

        return frame
