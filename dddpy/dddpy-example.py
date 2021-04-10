from dddpy.media.engine import DMediaEngine

from dddpy.media.video_processors import DVideoProcFreeze
from dddpy.media.video_processors import DVideoProcGrayscale
from dddpy.media.video_processors import DVideoProcDateTime


def main():

    media_engine = DMediaEngine(close_key='q')

    media_engine.add_video_proc(DVideoProcFreeze(), toggle_key='f')
    media_engine.add_video_proc(DVideoProcGrayscale(), toggle_key='b')
    media_engine.add_video_proc(DVideoProcDateTime("%d/%m/%Y %H:%M:%S"), toggle_key='t')

    try:

        media_engine.open_webcam()
        media_engine.print_command_keys()

        for frame in media_engine.frames():
            if not media_engine.show(frame, window_name='deep-vision-4u'):
                break

    except AssertionError as ex:
        print('Exception:', ex)
        exit(1)

    media_engine.release()


if __name__ == '__main__':
    main()
