from vision import FaceDetector
import midi_1_filter_freq_q as m
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def main():
    fd = FaceDetector()
    fd.start()
    try:
        while True:
            faces = fd.detect()
            if len(faces) > 0:
                # logging.info('%d faces: %s', len(faces), faces)
                face_x = ((200 - faces[0][0])) / 310
                face_y = (110-(faces[0][2])) / 140
                print(face_y)
                m.xy_to_fq(face_x, face_y)
    except KeyboardInterrupt:
        pass
    finally:
        fd.stop()


if __name__ == '__main__':
    main()
