from backgorund_image import backgroundImage
from check_directory import add_path
def filter_background_image():
    type_filter = int(input('type_filter : '))
    background_filter =''
    color = ''
    type_of_background = input('enter type of background : [gray,image,blur,color] :  ')

    path_input_image=add_path(input('image path : '),'Input_image/')

    if type_filter ==0 and type_of_background == 'image' :
        background_filter = add_path(input('path image : '), 'input_background/')
        backgroundImage(type_of_background, path_input_image,color, background_filter)


    if type_of_background=='color':
        add_color = input('input color rgb : 0,0,255 : ')
        color = tuple(map(int, add_color.split(',')))

    if type_filter == 1 :
        backgroundImage(type_of_background,path_input_image,color,'../assest/background/back1.jpg')
    if type_filter == 2 :
        backgroundImage(type_of_background,path_input_image,background_filter,color,'../assest/background/back2.jpg')

filter_background_image()