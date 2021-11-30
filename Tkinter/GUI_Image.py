import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
from filters_image.change_filter import change_filter
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from filters_image.image_filtering_face import image_filtering_face
import cv2
from tkinter_custom_button import TkinterCustomButton
# root = tk.Tk()
images = []
count = 0
next = False
entry = ""
######### import Window ##########



# mainloop()



def importWindowyahia(root):
    newWindow = Toplevel(root)
    def browse():
        global count


        filename = filedialog.askopenfilename(title="select File",
                                              filetypes = (("jpeg files","*.jpg"),("all files","*.*"),('png files', '*.png')))
        images.append(filename)
        img = Image.open(images[-1])
        img = img.resize((500, 500))
        img = ImageTk.PhotoImage(img)
        img_label = Label(newWindow, image=img)
        img_label.photo = img
        img_label.place(x=228, y=40)

        filtering = TkinterCustomButton(master=newWindow,text="Add Filter", corner_radius=5,command=lambda: image_filter(filename, newWindow),
                                        fg_color="#FF5C58",hover_color="#ff544f", width=200,cursor="shuttle", text_font=("sans-serif", 20))
        filtering.place(x=380, y=550)




    root.withdraw()
    newWindow.title("New Window")
    newWindow.geometry("960x630")
    browse_button = TkinterCustomButton(master=newWindow,text="Browse", corner_radius=5, command=browse,
                        fg_color="#FF5C58",hover_color="#ff544f", width=200, cursor="shuttle",
                        text_font=("sans-serif", 20))


    browse_button.pack()


    ######## Back to previous window ########
    def on_closing():
        newWindow.destroy()
        root.deiconify()
    image= PhotoImage(file ='../assest/back.png')
    backButton = TkinterCustomButton(master=newWindow, corner_radius=15,
                        command=on_closing,fg_color="#f1f1f1",hover_color="#c1c1c1", cursor="shuttle",image=image,width=50)

    backButton.place(x=0,y=3)

    newWindow.protocol("WM_DELETE_WINDOW", on_closing)

    def render(image_withfilter):
        image_withfilter = cv2.cvtColor(image_withfilter, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image_withfilter)
        img = img.resize((500, 500))
        img = ImageTk.PhotoImage(img)
        img_label = Label(newWindow, image=img)
        img_label.photo = img
        img_label.place(x=228, y=40)
        # photo = ImageTk.PhotoImage(image=Image.fromarray(image_withfilter))
        # canvas.create_image(0, 0, anchor="nw", image=photo)

    def next_fun(path):
        global count

        images.append(image_filtering_face(
            change_filter[count]['filter'],
            path,
            change_filter[count]['center'],
            change_filter[count]['width'],
            change_filter[count]['height'],
            change_filter[count]['up'],
            change_filter[count]['left'],
            change_filter[count]['counte']
        ))
        count += 1
        if count == len(change_filter) - 1:
            count = 0
        render(images[-1])

    def submit(content,top):
        global entry
        entry1 = entry.get()
        imgdir = f"../saved/{entry1}.png"
        cv2.imwrite(imgdir, content)
        entry.delete(0, END)
        top.destroy()
    def saving(content, newWindow):
        pass
    def image_filter(path, newWindow):
        images.append(
            image_filtering_face(["../assest/tongue.png"], path, [57], [0.6], [1.2], [-25], [0],
                                 [0]))
        save = TkinterCustomButton(master=newWindow, text="Save", corner_radius=5,
                                   command=lambda: open_popup(images[-1],newWindow), fg_color="#FF5C58",hover_color="#ff544f", width=200, cursor="shuttle", text_font=("sans-serif", 20))
        save.place(x=50, y=550)
        next = TkinterCustomButton(master=newWindow, text="Next", corner_radius=5,
                                   command=lambda: next_fun(path), fg_color="#FF5C58",hover_color="#ff544f", width=200, cursor="shuttle", text_font=("sans-serif", 20))
        newWindow.bind("<Right>", lambda x: next_fun(path))
        next.place(x=710, y=550)
        render(images[-1])

    def open_popup(content,newWindow):
        top = Toplevel(newWindow)
        top.geometry("250x150")
        top.title("save")
        global entry
        sub_btn = TkinterCustomButton(master=top, text="Submit", corner_radius=5, command=lambda: submit(content,top),
                                      fg_color="#2da44e",hover_color="#24843f", width=100,
                                      cursor="shuttle", text_font=("sans-serif", 20))
        entry = tk.Entry(top, width=20, bg="white")
        entry.place(x=75, y=10)
        sub_btn.place(x=75, y=50)
