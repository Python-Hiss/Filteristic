# import cv2
# import numpy as np
# import dlib
# from math import hypot
# filter_image = cv2.imread("../assest/flower-crown-png-42606.png")
#
# # Loading Face detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#
# cap = cv2.VideoCapture(0)
#
# while True :
#     _, frame = cap.read()
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = detector(frame)
#     for face in faces :
#         landmarks = predictor(gray_frame, face)
#         top_glasses = (landmarks.part(24).x , landmarks.part(24).y)
#         left_glasses = (landmarks.part(0).x , landmarks.part(0).y)
#         right_glasses  = (landmarks.part(16).x , landmarks.part(16).y)
#         center_glasses = (landmarks.part(27).x , landmarks.part(27).y)
#
#         glasses_width = int (hypot(left_glasses[0] -right_glasses[0],
#                               left_glasses[1] - right_glasses[1]))
#
#         glasses_height = int(glasses_width * 0.6)
#
#         # positios
#         upper_left = (int(center_glasses[0] - glasses_width/2 ),
#                                int(center_glasses[1] - glasses_height/2))
#         lower_right = (int(center_glasses[0] + glasses_width / 2),
#                        int(center_glasses[1] + glasses_height / 2))
#
#         # Adding the glasses in the correct position
#         glasses = cv2.resize(filter_image,(glasses_width , glasses_height))
#         gray_glasses = cv2.cvtColor(glasses, cv2.COLOR_BGR2GRAY)
#
#
#         _, glasses_mask = cv2.threshold(gray_glasses,120, 225, cv2.THRESH_BINARY_INV)
#         glasses_area = frame[upper_left[1] : upper_left[1]+glasses_height , upper_left[0]:upper_left[0]+glasses_width]
#         glasses_ares_no_glasses = cv2.bitwise_and(glasses_area , glasses_area,mask= glasses_mask)
#         final_glasses = cv2.add(glasses_ares_no_glasses, glasses)
#         frame[upper_left[1]: upper_left[1] + glasses_height, upper_left[0]:upper_left[0] + glasses_width] = final_glasses
#
#     cv2.imshow("Frame",frame)
#
#
#
#     key = cv2.waitKey(1)
#     if key ==27 :
#         break