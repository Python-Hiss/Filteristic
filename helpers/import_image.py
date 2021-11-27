import cv2
import dlib
from math import hypot

path = r"snapchat-filters-png-4068.png"
filter_image = cv2.imread(path)
# Loading Face detector
detector = dlib.get_frontal_face_detector()
predictor_path = r"shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
image = cv2.imread('faces2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = detector(image)

for face in faces:
    landmarks = predictor(gray, face)

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
                int(center_filter[1] - filter_height / 2 + 25))
    bottom_right = (int(center_filter[0] + filter_width / 2),
                    int(center_filter[1] + filter_height / 2))

    # Adding the new filter
    # coloring
    filtery = cv2.resize(filter_image, (filter_width, filter_height))
    filtery_gray = cv2.cvtColor(filtery, cv2.COLOR_BGR2GRAY)
    _, filter1 = cv2.threshold(filtery_gray, 25, 255, cv2.THRESH_BINARY_INV)

    filter_area = image[top_left[1]: top_left[1] + filter_height, top_left[0]: top_left[0] + filter_width]
    filter_area_no_filter = cv2.bitwise_and(filter_area, filter_area, mask=filter1)
    final_filter = cv2.add(filter_area_no_filter, filtery)

    image[top_left[1]: top_left[1] + filter_height,
    top_left[0]: top_left[0] + filter_width] = final_filter

cv2.imshow("Frame", image)
cv2.waitKey(0)





