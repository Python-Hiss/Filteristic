import cv2
import numpy as np
import dlib
from math import hypot
filter_image = cv2.imread("assest/cat-ears.png")
filter_image3 = cv2.imread("assest/cat-nose.png")
# filter_image4 = cv2.imread("assest\eye1.png")
# filter_image5 = cv2.imread("assest\eye2.png")


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
        filter(frame,gray_frame,faces,filter_image,27,27,1.7,0.5,120)
        filter(frame, gray_frame, faces, filter_image3,28,28,1.1,1,0)

        # filter(frame, gray_frame, faces, filter_image3,27,27,1.5,1,100)
        # filter(frame, gray_frame, faces, filter_image4,40,40,0.2,0.4,5)
        # filter(frame, gray_frame, faces, filter_image5,46,46,0.2,0.4,5)



    except:
        _, frame_f = cap.read()
        cv2.imshow("Frame", frame_f)
    # else:
    #     _, frame_f = cap.read()
    #     cv2.imshow("Frame", frame_f)
def filter(frame,gray_frame,faces,filter_image1,X,Y,width,height,above=0,left=0):
    for face in faces:
        landmarks = predictor(gray_frame, face)

        # filter coordinates
        # top_filter = (landmarks.part(27).x+10, landmarks.part(24).y+10)
        center_filter = (landmarks.part(X).x-left, landmarks.part(Y).y-above)
        left_filter = (landmarks.part(4).x, landmarks.part(4).y)
        right_filter = (landmarks.part(14).x, landmarks.part(14).y)

        filter_width = int(hypot(left_filter[0] - right_filter[0],
                                 left_filter[1] - right_filter[1]) * width)
        filter_height = int(filter_width * height)

        # New filter position
        top_left = (int(center_filter[0] - filter_width / 2),
                    int(center_filter[1] - filter_height / 2))
        bottom_right = (int(center_filter[0] + filter_width / 2),
                        int(center_filter[1] + filter_height / 2))

        # Adding the new filter
        # coloring
        filtery = cv2.resize(filter_image1, (filter_width, filter_height))
        filtery_gray = cv2.cvtColor(filtery, cv2.COLOR_BGR2GRAY)
        _, filter1 = cv2.threshold(filtery_gray, 25, 255, cv2.THRESH_BINARY_INV)

        filter_area = frame[top_left[1]: top_left[1] + filter_height,
                      top_left[0]: top_left[0] + filter_width]
        filter_area_no_filter = cv2.bitwise_and(filter_area, filter_area, mask=filter1)
        final_filter = cv2.add(filter_area_no_filter, filtery)

        frame[top_left[1]: top_left[1] + filter_height,
        top_left[0]: top_left[0] + filter_width,:] = final_filter

        cv2.imshow("Frame", frame)