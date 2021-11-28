import cv2
import numpy as np
import dlib
from math import hypot
from change_filter import change_filter
import os

# Loading Face detector

def image_filtering_face(path_filter,center,width,height,up,left,counte=0):
    # path = r"../assest/moustache2.png"
    filter_image = []
    for i in path_filter:
        filter_image.append(cv2.imread(i))

    image = cv2.imread("saved/test.jpg")
    rows, cols, _ = image.shape
    filter1 = np.zeros((rows, cols), np.uint8)
    filter1.fill(0)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(image)
    if faces:
        try:
            for i in range(len(path_filter)):
                filter(image,gray_image,faces,filter_image[i],center[i],width[i],height[i],up[i],left[i])
        except:
            image = cv2.imread("saved/test.jpg")
            cv2.imshow("Frame", image)

    key = cv2.waitKey(0)
    if key == ord('n'):
        change_image(counte)
    elif key == ord('q'):
        cv2.destroyAllWindows()
    elif key == ord("c"):
        img_name = "../saved/opencv_frame.png"
        cv2.imwrite(img_name, image)
        print("{} written!".format(img_name))

        image = cv2.imread(img_name)
        cv2.imshow("Frame", image)
        key = cv2.waitKey(0)
        os.remove("../saved/opencv_frame.png")
        if key == ord("s"):
            user_name = input("enter name")
            imgdir = f"../saved/{user_name}.png"
            cv2.imwrite(imgdir, image)
            image_filtering_face(["../assest/tongue.png"],"../assest/face.jpg",[57],[0.6],[1.2],[-25],[0])
        if key == ord("e"):
            image_filtering_face(["../assest/tongue.png"],"../assest/face.jpg",[57],[0.6],[1.2],[-25],[0])



def filter(image,gray_frame,faces,filter_image1,center,width,height,up=0,left=0):
    predictor_path = r"../assest/shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_path)

    for face in faces:
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

        cv2.imshow("Frame", image)

def change_image(i):
    image_filtering_face(
        change_filter[i]['filter'],
        change_filter[i]['center'],
        change_filter[i]['width'],
        change_filter[i]['height'],
        change_filter[i]['up'],
        change_filter[i]['left'],
        change_filter[i]['counte']
    )
if __name__ == "__main__":
    image_filtering_face(["../assest/tongue.png"],[57],[0.6],[1.2],[-25],[0])