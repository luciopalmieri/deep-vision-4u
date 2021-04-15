import cv2
import pyvirtualcam
import numpy as np
from dddpy.media.video_processors import DVideoProc


class DMediaEngine:

    def __init__(self, close_key: str = 'q'):
        self.__video_cap = None
        self.__video_cap_width = None
        self.__video_cap_height = None
        self.__close_key = close_key
        self.__video_proc_list = []
        self.__virtual_cam = None

    def add_video_proc(self, video_proc: DVideoProc, toggle_key: str = None) -> int:

        """

        Add a Video Processor.

        :param video_proc: a DVideoProc subclass
        :param toggle_key: a keyboard key to activate/deactivate the processor when you use show()
        :return: video_proc_dict id (eg. use it to activate/deactivate the processor when you don't use show()
                 and toggle_key)

        """

        video_proc_dict = {
            'video_proc': video_proc,
            'active': False
        }

        if toggle_key:
            video_proc_dict['toggle_key'] = toggle_key

        self.__video_proc_list.append(video_proc_dict)

        return id(video_proc_dict)

    def open_webcam(self):
        self.__video_cap = cv2.VideoCapture(0)
        ret, frame = self.__video_cap.read()
        assert ret, "WebCam not available"
        self.__video_cap_width = frame.shape[1]
        self.__video_cap_height = frame.shape[0]

    def virtual_cam_set(self, width: float = None, height: float = None, fps: float = 15.0):
        width = width or self.__video_cap_width
        height = height or self.__video_cap_height

        if not width == self.__video_cap_width or not height == self.__video_cap_height:
            raise Exception("TODO Resize video capture frames size to virtual cam frames size")
            pass

        self.__virtual_cam = pyvirtualcam.Camera(width=width, height=height, fps=fps)

    def virtual_cam_send(self, frame: np.ndarray):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.__virtual_cam.send(frame)
        self.__virtual_cam.sleep_until_next_frame()

    def frames(self):
        return self.__FramesIterator(self.__video_cap, self.__video_proc_list)

    def release(self):
        if self.__video_cap:
            self.__video_cap.release()
        cv2.destroyAllWindows()

    def show(self, frame: np.ndarray, window_name: str = 'dddpy.media') -> bool:
        cv2.imshow(window_name, frame)

        key_code = cv2.waitKey(1)
        if key_code == ord(self.__close_key):
            return False

        self.__toggle_processor_by_keyboard(key_code)

        return True

    def print_command_keys(self):
        print('\n')
        print(f"- use '{self.__close_key}' to close the application")

        for video_proc_dict in self.__video_proc_list:
            toggle_key = video_proc_dict['toggle_key']
            video_proc = video_proc_dict['video_proc']
            print(f"- use '{toggle_key}' to activate/deactivate the {video_proc}")

    def __toggle_processor_by_keyboard(self, key_code: str):
        for video_proc_dict in self.__video_proc_list:
            toggle_key = video_proc_dict['toggle_key']
            if toggle_key and key_code == ord(toggle_key):
                video_proc_dict['active'] = not video_proc_dict['active']
                break

    class __FramesIterator:

        def __init__(self, video_capture, video_proc_list):
            self.__video_cap = video_capture
            self.__video_proc_list = video_proc_list

        def __iter__(self):
            return self

        def __next__(self):
            if not self.__video_cap.isOpened():
                raise StopIteration

            _, frame = self.__video_cap.read()
            frame = self.__process_frame(frame)

            return frame

        def __process_frame(self, frame):
            for video_proc_dict in self.__video_proc_list:
                active = video_proc_dict['active']
                video_proc = video_proc_dict['video_proc']
                video_proc.activate = active
                frame = video_proc.process(frame)

            return frame
