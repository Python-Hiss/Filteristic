import cv2
import numpy as np
import dlib
from math import hypot
from change_filter import change_filter
# change_filter =[{'filter':['../assest/hair9.png','../assest/ghoul2.png'],'center':[27,66],'width':[1.5,1],'height':[1,1],'up':[100,20],'left':[0,0]}]
cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
filter1 = np.zeros((rows, cols), np.uint8)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
counte=0
def video_filtering_face(path,center,width,height,up,left,counte=0):

    filter_image = []
    for i in path:
        filter_image.append(cv2.imread(i))


    while cap.isOpened():
        filter1 = np.zeros((rows, cols), np.uint8)

        _, frame = cap.read()
        filter1.fill(0)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(frame)
        if faces:
            try:
                for i in range(len(path)):
                    filter(frame,gray_frame,faces,filter_image[i],center[i],width[i],height[i],up[i],left[i])
            except:
                _, frame_f = cap.read()
                cv2.imshow("Frame", frame_f)
        else:
            _, frame_f = cap.read()
            cv2.imshow("Frame", frame_f)
        key = cv2.waitKey(1)
        if key == ord('n'):
            # print('first : ' ,i)
            change_image(counte)
            # print('second : ', i)



def filter(frame,gray_frame,faces,filter_image1,center,width,height,up=0,left=0):
    for face in faces:
        landmarks = predictor(gray_frame, face)

        # filter coordinates
        # top_filter = (landmarks.part(27).x+10, landmarks.part(24).y+10)
        # if yahia:
        #     up = (landmarks.part(8).y - landmarks.part(62).y) * 3
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
