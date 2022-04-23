import cvlib
import cv2
import os
import tensorflow
import datetime

IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.tiff', '.gif']
VID_EXTENSIONS = ['.mov', '.mp4', '.avi', '.mpg', '.mpeg', '.m4v', '.mkv']

human_detected=False
valid_file_alert= False
error_alert= False
def humanDetect(file_name, save_directory, yolo='yolov4', continuous=False, nth_frame=10, confidence=.65, gpu=False):

 global valid_file_alert

 #for human detection 
 is_humandetect=False
 is_valid=False

 if os.path.splitext(file_name)[1] in IMG_EXTENSIONS:
     # to check if the extension of the the file in there in IMG_Extensions or not
     frame=cv2.imread(file_name) #to read the image from the location


