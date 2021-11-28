from os.path import exists
import os
import cv2
import requests
def check_image():
    path = input('enter the name of path output : ')
    path_image = f'Output_image/{path}.png'
    file_exists = exists(path_image)
    while file_exists:
        path_name2 = input('this name is exist try another one or enter q : ')
        if path_name2 == 'q':
            path_image = False
            break

        path_image = f'Output_image/{path_name2}.png'
        file_exists = exists(path_image)
    return path_image

def saveimage(path):
    print("close the window for image")
    image = cv2.imread(path)
    cv2.imshow('image window', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save = input('do you want to save image ?')
    if not save == 'yes':
        os.remove(path)
    return
def add_path(image_path,origin):

    path_image = file_exist(origin)

    if ':' in image_path and "\\" in image_path  and 'http' not in image_path:
        img = cv2.imread(image_path)
        cv2.imwrite(path_image, img)

    else:
        r= requests.get(image_path)
        with open(path_image,'wb') as f :
            f.write(r.content)

    return path_image

def file_exist(origin):
    path_name = input('add path name : ')
    path_image = f'{origin}{path_name}.png'
    file_exists = exists(path_image)
    while file_exists:
        path_name2 = input('this name is exist try another one or enter q : ')
        if path_name2 == 'q':
            path_image = ''
            break

        path_image = f'{origin}{path_name2}.png'
        file_exists = exists(path_image)
    return path_image