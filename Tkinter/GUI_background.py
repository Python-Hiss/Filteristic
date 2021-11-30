import os
from tkinter import *
from tkinter import ttk, filedialog
import cv2
import requests
from PIL import Image, ImageTk
from background_image.backgorund_image import backgroundImage
root = Tk()
images = []
filter_type = ""

path_name = ""
def get_filter_type():

    global filter_type, path_name
    filter_type = type_choosen.get()
    if filter_type == "color":
        apply()
    elif filter_type == "image":
        filename = filedialog.askopenfilename(title="select File",
                                              filetypes=(
                                                  ("jpeg files", "*.jpg"), ("all files", "*.*"),
                                                  ('png files', '*.png')))
        backgroundImage(filter_type, images[-1], 0, filename)
        render("../saved/temp.png")
    else:
        backgroundImage(filter_type, images[-1], 0, '../assest/background/back1.png')
        render("../saved/temp.png")


def apply():
    def apply_color():
        b = {'Black':(0,0,0),'Green':(0,255,0),'White':(255,255,255),'Blue':(0,0,255),'Red':(255,0,0)}
        backgroundImage("color", images[-1], b[color_choosen.get()], '../assest/background/back1.png')
        render("../saved/temp.png")
    colorButton = Button(text="Add color", padx=10, pady=10, fg="white", bg="#2596be", font=('arial', 15),
                         command=apply_color)
    colorButton.grid(row=4, column=3)
    m = StringVar()
    color_choosen = ttk.Combobox(width=20, textvariable=m)
    color_choosen['values'] = ('Black',
                               'Green',
                               'White',
                               'Blue',
                               'Red')

    color_choosen.grid(column=2, row=4)
    color_choosen.current(1)






def add_from_web():
    img_url = entry.get()
    entry.delete(0, END)
    r = requests.get(img_url)
    with open("../saved/web.png", 'wb') as f:
        f.write(r.content)
    images.append("../saved/web.png")
    render(images[-1])



def render(image_withfilter):
    img = Image.open(image_withfilter)
    img = img.resize((500, 500))
    img = ImageTk.PhotoImage(img)
    img_label = Label(root, image=img)
    img_label.photo = img
    img_label.grid(row=0, column=0)

def browse():
    filename = filedialog.askopenfilename(title="select File",
                                          filetypes=(
                                          ("jpeg files", "*.jpg"), ("all files", "*.*"), ('png files', '*.png')))
    images.append(filename)
    render(images[-1])


def saving():
    os.rename("../saved/temp.png", f"../saved/{entryy.get()}.png")
    entryy.delete(0,END)


importButton = Button(text="Import", padx=10, pady=10, fg="white", bg="#2596be", font=('arial', 15), command=browse)
importButton.grid(row=0, column=3)

web_link_Button = Button(text="import web link", padx=10, pady=10, fg="white", bg="#2596be", font=('arial',15), command=add_from_web)
web_link_Button.grid(row=1, column=2)

typeButton = Button(text="Apply Filter", padx=10, pady=10, fg="white", bg="#2596be", font=('arial', 10), command=get_filter_type)
typeButton.grid(row=2, column=3)

saveButton = Button(text="Save", padx=10, pady=10, fg="white", bg="#2596be", font=('arial',15), command=saving)
saveButton.grid(row=3, column=2)

entry = Entry(width=20, bg="white")
entry.grid(row=1, column=1)
entryy = Entry(width=20, bg="white")
entryy.grid(row=3, column=1)

# label
ttk.Label(text="Select filter type :",
          font=("Times New Roman", 10)).grid(column=1,
                                             row=2, padx=10, pady=10)

n = StringVar()
type_choosen = ttk.Combobox(width=20, textvariable=n)

# Adding combobox drop down list
type_choosen['values'] = ('image',
                          'gray',
                          'blur',
                          'color',)

type_choosen.grid(column=2, row=2)
type_choosen.current(2)

root.mainloop()