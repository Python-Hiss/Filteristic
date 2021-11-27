import cv2
import numpy as np
import dlib
from math import hypot

def video_filtering_face(path,center,width,height,up=0,left=0,yahia = False):
    filter_path = path
    filter_image = cv2.imread(filter_path)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    rows, cols, _ = frame.shape
    filter1 = np.zeros((rows, cols), np.uint8)
    while cap.isOpened():
        _, frame = cap.read()
        filter1.fill(0)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(frame)
        if faces:
            try:

                for face in faces:
                    landmarks = predictor(gray_frame, face)

                    # filter coordinates
                    if yahia:
                        up = (landmarks.part(8).y - landmarks.part(62).y)*3
                    center_filter = (landmarks.part(center).x-left, landmarks.part(center).y-up)
                    left_filter = (landmarks.part(3).x, landmarks.part(3).y)
                    right_filter = (landmarks.part(13).x, landmarks.part(13).y)

                    filter_width = int(hypot(left_filter[0] - right_filter[0],
                                             left_filter[1] - right_filter[1]) * width)
                    filter_height = int(filter_width *height)

                    # New filter position
                    top_left = (int(center_filter[0] - filter_width / 2),
                                int(center_filter[1] - filter_height / 2))
                    bottom_right = (int(center_filter[0] + filter_width / 2),
                                    int(center_filter[1] + filter_height / 2))

                    # Adding the new filter
                    # coloring
                    filtery = cv2.resize(filter_image, (filter_width, filter_height))
                    filtery_gray = cv2.cvtColor(filtery, cv2.COLOR_BGR2GRAY)

                    _, filter1 = cv2.threshold(filtery_gray, 25, 255, cv2.THRESH_BINARY_INV)

                    filter_area = frame[top_left[1]: top_left[1] + filter_height,
                                  top_left[0]: top_left[0] + filter_width]
                    filter_area_no_filter = cv2.bitwise_and(filter_area, filter_area, mask=filter1)
                    final_filter = cv2.add(filter_area_no_filter, filtery)

                    frame[top_left[1]: top_left[1] + filter_height,
                    top_left[0]: top_left[0] + filter_width] = final_filter

                    cv2.imshow("Frame", frame)
            except:
                _, frame_f = cap.read()
                cv2.imshow("Frame", frame_f)
        else:
            _, frame_f = cap.read()
            cv2.imshow("Frame", frame_f)
        key = cv2.waitKey(1)
        if key == 27:
            break