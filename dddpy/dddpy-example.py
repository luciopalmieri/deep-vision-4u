from dddpy.media.engine import DMediaEngine
from dddpy.media.video_processors import DVideoProcGrayscale


def main():

    media_engine = DMediaEngine()

    # add_video_processor return the id(video_proc_dict) that can be used to programmatically toggle the processor
    #   activation without using the toggle_key
    media_engine.add_video_processor(DVideoProcGrayscale(), toggle_key='b')

    try:

        media_engine.open_webcam()

        for frame in media_engine.frames():
            if not media_engine.show(frame, window_name='deep-vision-4u', close_key='q'):
                break

    except AssertionError as ex:
        print('Exception:', ex)
        exit(1)

    media_engine.release()


if __name__ == '__main__':
    main()