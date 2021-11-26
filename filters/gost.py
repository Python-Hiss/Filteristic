import cv2
import numpy as np
import dlib
from math import hypot
filter_image = cv2.imread("assest/10-2-moustache-free-png-image.png")

# Loading Face detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("assest\shape_predictor_68_face_landmarks.dat")

def filteringmouse(cap,rows, cols):
    filter1 = np.zeros((rows, cols), np.uint8)
    _, frame = cap.read()
    filter1.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(frame)

    # if faces:
    try:
        filter(frame)
        # filter(frame, gray_frame, faces, filter_image3,27,27,1.5,2,25)
    except:
        _, frame_f = cap.read()
        cv2.imshow("Frame", frame_f)
    # else:
    #     _, frame_f = cap.read()
    #     cv2.imshow("Frame", frame_f)
def filter(frame):
        invert = cv2.bitwise_not(frame)
        cv2.imshow("Frame", invert)