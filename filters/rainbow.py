import cv2
import numpy as np
import dlib
from math import hypot
path = r"assest\snapchat-filters-png-4068.png"
filter_image = cv2.imread(path)
# Loading Face detector
detector = dlib.get_frontal_face_detector()
predictor_path = r"assest\shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)


def rainbow_filtering(cap,rows, cols):
    filter1 = np.zeros((rows, cols), np.uint8)
    _, frame = cap.read()
    filter1.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(frame)
    # if faces:
    try:

        for face in faces:
            landmarks = predictor(gray_frame, face)

            # filter coordinates
            # top_filter = (landmarks.part(27).x, landmarks.part(24).y)
            center_filter = (landmarks.part(57).x, landmarks.part(57).y)
            left_filter = (landmarks.part(2).x, landmarks.part(2).y)
            right_filter = (landmarks.part(14).x, landmarks.part(14).y)

            filter_width = int(hypot(left_filter[0] - right_filter[0],
                                     left_filter[1] - right_filter[1]) * 0.9)
            filter_height = int(filter_width * 1.3)

            # New filter position
            top_left = (int(center_filter[0] - filter_width / 2),
                        int(center_filter[1] - filter_height / 2 + 20))
            bottom_right = (int(center_filter[0] + filter_width / 2),
                            int(center_filter[1] + filter_height / 2))

            # Adding the new filter
            # coloring
            filtery = cv2.resize(filter_image, (filter_width, filter_height))
            filtery_gray = cv2.cvtColor(filtery, cv2.COLOR_BGR2GRAY)
            _, filter1 = cv2.threshold(filtery_gray, 25, 255, cv2.THRESH_BINARY_INV)

            filter_area = frame[top_left[1]: top_left[1] + filter_height, top_left[0]: top_left[0] + filter_width]
            filter_area_no_filter = cv2.bitwise_and(filter_area, filter_area, mask=filter1)
            final_filter = cv2.add(filter_area_no_filter, filtery)

            frame[top_left[1]: top_left[1] + filter_height,
            top_left[0]: top_left[0] + filter_width] = final_filter

            cv2.imshow("Frame", frame)
    except:
        _, frame_f = cap.read()
        cv2.imshow("Frame", frame_f)
    # else:
    #     _, frame_f = cap.read()
    #     cv2.imshow("Frame", frame_f)