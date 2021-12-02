import pixellib
from background_image.check_directory import saveimage, check_image
from pixellib.tune_bg import alter_bg


def backgroundImage(type, input_image, color, back_ground):
    path_name = "../saved/temp.png"
    if path_name:
        change_bg = alter_bg(model_type = "pb")
        change_bg.load_pascalvoc_model("../background_image/xception_pascalvoc.pb")

        if type == 'image':
            change_bg.change_bg_img(f_image_path = input_image, b_image_path = back_ground, output_image_name=path_name,detect='person')
        if type == 'gray':
            change_bg.gray_bg(input_image, output_image_name=path_name)
        if type =='color':
            change_bg.color_bg(input_image, colors=color, output_image_name=path_name)
        if type == 'blur':
            change_bg.blur_bg(input_image, low=True, output_image_name=path_name)
        # saveimage(path_name)


# backgroundImage('gray','Output_image/test2.png','Input_image/lena.jpg')
