from background_live import background
from request_image import add_path,check_image

type_filter = (input('add new background [yes,no] ? '))
type_blur=int(input('number for blur start from 1 : '))
if type_filter == 'yes':
    add_path(input('path image : '))

img =check_image()
background('../assest/background/back1.png',type_blur,img)
