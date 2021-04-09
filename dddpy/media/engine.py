import cv2


class DMediaEngine:

    def __init__(self):
        self.__video_cap = None

    def open_webcam(self):
        self.__video_cap = cv2.VideoCapture(0)
        ret, _ = self.__video_cap.read()
        assert ret, "WebCam not available"

    def frames(self):
        return DFramesIterator(self.__video_cap)

    def release(self):
        if self.__video_cap:
            self.__video_cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def show(frame, window_name='dddpy.media', close_key='q'):
        cv2.imshow(window_name, frame)
        k = cv2.waitKey(1)
        if k == ord(close_key):
            return False
        return True


class DFramesIterator:

    def __init__(self, video_capture):
        self.__video_cap = video_capture

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__video_cap.isOpened():
            raise StopIteration

        _, frame = self.__video_cap.read()

        return frame
