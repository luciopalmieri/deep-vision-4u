import cv2


class DMediaEngine:

    def __init__(self, close_key='q'):
        self.__video_cap = None
        self.__close_key = close_key
        self.__video_proc_list = []

    def add_video_processor(self, video_proc, toggle_key=None):
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
        ret, _ = self.__video_cap.read()
        assert ret, "WebCam not available"

    def frames(self):
        return self.__FramesIterator(self.__video_cap, self.__video_proc_list)

    def release(self):
        if self.__video_cap:
            self.__video_cap.release()
        cv2.destroyAllWindows()

    def show(self, frame, window_name='dddpy.media'):
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
            print(f"- use '{video_proc_dict['toggle_key']}' to activate/deactivate the {video_proc_dict['video_proc']}")

    def __toggle_processor_by_keyboard(self, key_code):
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
                if video_proc_dict['active']:
                    frame = video_proc_dict['video_proc'].process(frame)

            return frame
