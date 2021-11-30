import os
from tkinter import *
from tkinter import ttk, filedialog
import requests
from PIL import Image, ImageTk
from background_image.backgorund_image import backgroundImage
from tkinter_custom_button import TkinterCustomButton
images = []
filter_type = ""
path_name = ""

def background_window(window_root):
    window = Toplevel(window_root)
    window_root.withdraw()
    window.title("Import Window")
    window.geometry("1000x700")
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

    def on_closing():
        window.destroy()
        window_root.deiconify()

    image = PhotoImage(file='../assest/back.png')
    backButton = TkinterCustomButton(master=window, corner_radius=15,
                                     command=on_closing, fg_color="#f1f1f1", hover_color="#c1c1c1", cursor="shuttle",
                                     image=image, width=50)

    backButton.place(x=0, y=3)

    window.protocol("WM_DELETE_WINDOW", on_closing)

    def apply():
        def apply_color():
            b = {'Black':(0,0,0),'Green':(0,255,0),'White':(255,255,255),'Blue':(0,0,255),'Red':(255,0,0)}
            backgroundImage("color", images[-1], b[color_choosen.get()], '../assest/background/back1.png')
            render("../saved/temp.png")
        colorButton = TkinterCustomButton(master= window, text="Add color", corner_radius=5,
                            command=apply_color,fg_color="#FF5C58",hover_color="#ff544f", width=200,
                            cursor="shuttle", text_font=("sans-serif", 16))
        colorButton.place(x=510, y=550)
        m = StringVar()
        color_choosen = ttk.Combobox(window, width=20, textvariable=m)
        color_choosen['values'] = ('Black',
                                   'Green',
                                   'White',
                                   'Blue',
                                   'Red')

        color_choosen.place(x=720, y=559)
        color_choosen.current(2)


    def add_from_web():
        img_url = entry.get("1.0","end-1c")
        r = requests.get(img_url)
        with open("../saved/web.png", 'wb') as f:
            f.write(r.content)
        images.append("../saved/web.png")
        render(images[-1])
        common()


    def render(image_withfilter):
        img = Image.open(image_withfilter)
        img = img.resize((720, 480))
        img = ImageTk.PhotoImage(img)
        img_label = Label(window, image=img)
        img_label.photo = img
        img_label.place(x=140, y=60)

    def browse():
        filename = filedialog.askopenfilename(title="select File",
                                              filetypes=(
                                              ("jpeg files", "*.jpg"), ("all files", "*.*"), ('png files', '*.png')))
        images.append(filename)
        render(images[-1])
        common()

    def saving(top):
        os.rename("../saved/temp.png", f"../saved/{entryy.get()}.png")
        entryy.delete(0,END)
        on_closing(top)

    def on_closing(top):
        top.destroy()
        window.deiconify()

    importButton = TkinterCustomButton(master=window, text="Browse", corner_radius=5,
                        command=browse, fg_color="#FF5C58",hover_color="#ff544f", width=200,
                        cursor="shuttle", text_font=("sans-serif", 20))
    importButton.place(x=140, y= 10)

    web_link_Button = TkinterCustomButton(master=window, text="Download", corner_radius=5,
                        command=add_from_web,fg_color="#FF5C58",hover_color="#ff544f", width=200,
                        cursor="shuttle", text_font=("sans-serif", 20))
    web_link_Button.place(x=660, y= 10)

    entry = Text(window, width=27, height=2, bg="white")
    entry.place(x=435, y= 13)
    entry.insert(END, 'Enter image link from web')


    n = StringVar()
    type_choosen = ttk.Combobox(window, width=20, textvariable=n)

    def open_popup(newWindow):
        top = Toplevel(newWindow)
        top.geometry("250x150")
        top.title("save")
        sub_btn = TkinterCustomButton(master=top, text="Submit", corner_radius=5, command=lambda: saving(top),
                                      fg_color="#2da44e",hover_color="#24843f", width=100,
                                      cursor="shuttle", text_font=("sans-serif", 20))

        global entryy
        entryy = Entry(top, width=20, bg="white")
        entryy.place(x=65, y=13)
        sub_btn.place(x=75, y=50)

    def common():
        typeButton = TkinterCustomButton(master=window, text="Apply Filter", corner_radius=5,
                            command=get_filter_type, fg_color="#FF5C58",hover_color="#ff544f", width=200,
                            cursor="shuttle", text_font=("sans-serif", 16))
        typeButton.place(x=140, y=550)

        saveButton = TkinterCustomButton(master=window, text="Save", corner_radius=5,
                            command=lambda: open_popup(window), fg_color="#FF5C58",hover_color="#ff544f", width=200,
                            cursor="shuttle", text_font=("sans-serif", 20))
        saveButton.place(x=400, y=600)
        type_choosen['values'] = ('image',
                                  'gray',
                                  'blur',
                                  'color',)

        type_choosen.place(x=350, y=559)
        type_choosen.current(2)

