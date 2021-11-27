from background_live import background
from request_image import add_path,check_image
from os.path import exists

type_filter = int(input('type_filter : '))
type_blur=int(input('number for blur start from 1 : '))
if type_filter == 0:
    path,img = add_path(input('path image : '))
    background('../assest/background/back1.png', type_blur,img)
if type_filter ==1:
    img =check_image()
    print(img)
    background('../assest/background/back1.png',type_blur,img)
