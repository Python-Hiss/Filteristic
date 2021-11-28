import requests
from os.path import exists
import os
import cv2
def add_path(image_path):
    path_image=file_exist()
    if ':' in image_path and "\\" in image_path and 'http' not in image_path:
        print('hello')
        img = cv2.imread(image_path)
        cv2.imwrite(path_image, img)
    else:
        print('hi')
        r= requests.get(image_path)
        with open(path_image,'wb') as f :
            f.write(r.content)


def file_exist():
    img = 1
    path_image = f'../assest/background/back{img}.png'
    file_exists = exists(path_image)
    while file_exists :
        img+=1
        path_image = f'../assest/background/back{img}.png'
        file_exists = exists(path_image)
    return path_image

def check_image():
    img = 1
    path_image = f'../assest/background/back{img}.png'
    file_exists = exists(path_image)
    while file_exists:
        img += 1
        path_image = f'../assest/background/back{img}.png'
        file_exists = exists(path_image)
    return img-1

