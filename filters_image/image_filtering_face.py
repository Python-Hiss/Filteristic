import cv2
import numpy as np
import dlib
from math import hypot
# from filters_image.change_filter_image import change_filter
import os

def image_filtering_face(path_filter,path_img,center,width,height,up,left,counte=0):


    filter_image = []
    for i in path_filter:
        filter_image.append(cv2.imread(i))

    image = cv2.imread(path_img)
    rows, cols, _ = image.shape
    filter1 = np.zeros((rows, cols), np.uint8)
    filter1.fill(0)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(image)
    if faces:
        # try:
        for i in range(len(path_filter)):
            test = filter(image,gray_image,faces,filter_image[i],center[i],width[i],height[i],up[i],left[i])
        return test
        # except:
        #     image = cv2.imread(path_img)

        #     return image


def filter(image,gray_frame,faces,filter_image1,center,width,height,up=0,left=0):
    predictor_path = "../assest/shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_path)
    for face in faces:
        try:
            landmarks = predictor(gray_frame, face)

            center_filter = (landmarks.part(center).x-left, landmarks.part(center).y-up)
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
            filtery = cv2.resize(filter_image1, (filter_width, filter_height))
            filtery_gray = cv2.cvtColor(filtery, cv2.COLOR_BGR2GRAY)
            _, filter1 = cv2.threshold(filtery_gray, 25, 255, cv2.THRESH_BINARY_INV)

            filter_area = image[top_left[1]: top_left[1] + filter_height,
                          top_left[0]: top_left[0] + filter_width]
            filter_area_no_filter = cv2.bitwise_and(filter_area, filter_area, mask=filter1)
            final_filter = cv2.add(filter_area_no_filter, filtery)

            image[top_left[1]: top_left[1] + filter_height,
            top_left[0]: top_left[0] + filter_width,:] = final_filter
            print("filter1")
        except:
            print("except")
    return image
        # cv2.imshow("Frame", image)
        # key = cv2.waitKey(0)

