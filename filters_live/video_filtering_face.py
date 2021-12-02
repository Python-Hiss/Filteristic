import cv2
import numpy as np
import dlib
from math import hypot
from filters_live.change_filter import change_filter
import mediapipe as mp

import os
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../filters_live/shape_predictor_68_face_landmarks.dat")
counte=0
def video_filtering_face(path,center,width,height,up,left,path_back,blur,filter_face,background_face):

    filter_image = []
    for i in path:
        filter_image.append(cv2.imread(i))
    #
    _, frame = cap.read()
    rows, cols, _ = frame.shape
    filter1 = np.zeros((rows, cols), np.uint8)

    filter1.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(frame)
    if faces:
        try:
            if filter_face:
                for i in range(len(path)):
                    filter(frame,gray_frame,faces,filter_image[i],center[i],width[i],height[i],up[i],left[i])
            if background_face:
                frame =background(frame,path_back,blur )

        except:
            _, frame = cap.read()
    else:
        _, frame = cap.read()

    return frame


def filter(frame,gray_frame,faces,filter_image1,center,width,height,up=0,left=0):
    for face in faces:
        landmarks = predictor(gray_frame, face)


        center_filter = (landmarks.part(center).x-left, landmarks.part(center).y-up)
        left_filter = (landmarks.part(4).x, landmarks.part(4).y)
        right_filter = (landmarks.part(14).x, landmarks.part(14).y)

        filter_width = int(hypot(left_filter[0] - right_filter[0],
                                 left_filter[1] - right_filter[1]) * width)
        filter_height = int(filter_width * height)

        top_left = (int(center_filter[0] - filter_width / 2),
                    int(center_filter[1] - filter_height / 2))
        bottom_right = (int(center_filter[0] + filter_width / 2),
                        int(center_filter[1] + filter_height / 2))


        filtery = cv2.resize(filter_image1, (filter_width, filter_height))
        filtery_gray = cv2.cvtColor(filtery, cv2.COLOR_BGR2GRAY)
        _, filter1 = cv2.threshold(filtery_gray, 25, 255, cv2.THRESH_BINARY_INV)

        filter_area = frame[top_left[1]: top_left[1] + filter_height,
                      top_left[0]: top_left[0] + filter_width]

        filter_area_no_filter = cv2.bitwise_and(filter_area, filter_area, mask=filter1)
        final_filter = cv2.add(filter_area_no_filter, filtery)

        frame[top_left[1]: top_left[1] + filter_height,
        top_left[0]: top_left[0] + filter_width,:] = final_filter

        # cv2.imshow("Frame", frame)

def change_image(i):
    video_filtering_face(
        change_filter[i]['filter'],
        change_filter[i]['center'],
        change_filter[i]['width'],
        change_filter[i]['height'],
        change_filter[i]['up'],
        change_filter[i]['left'],
        change_filter[i]['counte']
    )

mp_selfie_segmentation = mp.solutions.selfie_segmentation
fsize = (480, 640)
def background(frame,path,blur =1):


    scene = cv2.imread(path)  # read the scene image
    scene = cv2.blur(scene, (blur, blur))
    scene = cv2.resize(scene, (fsize[1], fsize[0]))  # resize scene to the size of frame
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_seg:
        bg_image = scene
        # ret, frame = cap.read()
        # if not ret:
        #     print("Error reading frame...")

        frame = cv2.resize(frame, (fsize[1], fsize[0]))

        # flip it to look like selfie camera
        # frame = cv2.flip(frame, 1)

        # get rgb image to pass that on selfie segmentation
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # process it!
        results = selfie_seg.process(rgb)

        # get the condition from result's segmentation mask
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1

        # apply background change if condition matches
        output_image = np.where(condition, frame, bg_image)
        return output_image

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_filtering_face(["../assest/tongue.png"],[57],[0.6],[1.2],[-25],[0])