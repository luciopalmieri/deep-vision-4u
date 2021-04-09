from dddpy.media.engine import DMediaEngine


def main():

    media_engine = DMediaEngine()

    try:

        media_engine.open_webcam()

        for frame in media_engine.frames():
            if not DMediaEngine.show(frame, window_name='deep-vision-4u', close_key='q'):
                break

    except AssertionError as ex:
        print('Exception:', ex)
        exit(1)

    media_engine.release()


if __name__ == '__main__':
    main()
