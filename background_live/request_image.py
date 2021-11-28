import requests
from os.path import exists
def add_path(image_path):
    r= requests.get(image_path)
    img =1
    path_image = f'../assest/background/back{img}.png'
    file_exists = exists(path_image)
    while file_exists :
        img+=1
        path_image = f'../assest/background/back{img}.png'
        file_exists = exists(path_image)

    with open(path_image,'wb') as f :
        f.write(r.content)

    return path_image,img

def check_image():
    img = 1
    path_image = f'../assest/background/back{img}.png'
    file_exists = exists(path_image)
    while file_exists:
        img += 1
        path_image = f'../assest/background/back{img}.png'
        file_exists = exists(path_image)
    return img-1

