import cv2
import numpy as np
import dlib
from filters.filter1 import filtering
# from filters.dogfilter import filteringdog
from filters.mouse import filteringmouse

# Loading Camera and Nose image and Creating mask
cap = cv2.VideoCapture('baby.mp4')
cap.set(3, 1920)
cap.set(4, 1080)
_, frame = cap.read()
# print(frame)
rows, cols, _ = frame.shape
filter1 = np.zeros((rows, cols), np.uint8)
while True:
    filteringmouse(cap,rows, cols)
    key = cv2.waitKey(1)
    if key == 27:
        break