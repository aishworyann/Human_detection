import cvlib
import cv2
import os
import tensorflow
import datetime
import numpy as np

human_detected = False
error_alert = False


def humanDetect(save_directory, yolo='yolov4', continuous=False, nth_frame=10, confidence=.65, gpu=False):
    human_count = 0
    # for human detection
    is_humandetect = False
    is_valid = False
    analyze_error = False

    vid = cv2.VideoCapture(0)
    while (vid.isOpened()):
        while (True):
            # for video
            #           vid.set(cv2.CAP_PROP_POS_FRAMES,frame_number)                #will make a set of frames with their position
            ret , frame = vid.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(10) & 0xFF
            try:
                bbox, labels, conf = cvlib.detect_common_objects(frame, model=yolo, confidence=confidence,enable_gpu=gpu)
            except Exception as e:
                print(e)
                analyze_error = True
                pass

            if 'person' in labels:
                human_count += 1
                is_humandetect = True

                marked_frame = cv2.object_detection.draw_bbox(frame, bbox, labels, conf, write_conf=True)

                save_file_name = os.path.basename('screenshot' + '-' + str(person_detection_counter) + '.jpeg')
                cv2.imwrite(save_directory + '/' + save_file_name, marked_frame)

        vid.release()
        cv2.destroyAllWindows()
    else:
        print("Alert ! Camera disconnected")

location = '/Users/aishworyann/PycharmProjects/Human_detection/'
yolo_string = 'yolov4'

humanDetect(location,yolo_string)


