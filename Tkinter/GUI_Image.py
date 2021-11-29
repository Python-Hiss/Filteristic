import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
from filters_image.change_filter import change_filter
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from filters_image.image_filtering_face import image_filtering_face
import cv2
# root = tk.Tk()
images = []
count = 0
next = False
entry = ""
######### import Window ##########
def render(image_withfilter,canvas):
    image_withfilter = cv2.cvtColor(image_withfilter, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(image_withfilter))
    canvas.create_image(0, 0, anchor="nw", image=photo)\
            .grid(column=2, row=1, columnspan=2)
def next_fun(path,canvas):
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
    if count == len(change_filter)-1:
        count = -1
    render(images[-1],canvas)

def submit(content):
    global entry
    entry1 = entry.get()
    imgdir = f"../saved/{entry1}.png"
    cv2.imwrite(imgdir, content)
    entry.delete(0, END)
def saving(content,newWindow):
    global entry
    sub_btn = tk.Button(newWindow, text='Submit', command=lambda: submit(content))
    entry = tk.Entry(newWindow, width=20, bg="white")
    entry.grid(row=1, column=2)
    sub_btn.grid(row=2, column=2)

def image_filter(path, canvas, newWindow):
    print('yahia')
    images.append(
        image_filtering_face(["../assest/tongue.png"], path, [57], [0.6], [1.2], [-25], [0],
                             [0]))
    save = tk.Button(newWindow, text="save", padx=90, pady=10, fg="white", bg="#2596be",
                     font=('arial', 15), command=lambda: saving(images[-1],newWindow))
    save.grid(row=0, column=4)
    next = tk.Button(newWindow, text="next", padx=90, pady=10, fg="white", bg="#2596be",
                         font=('arial', 15), command=lambda: next_fun(path, canvas))
    next.grid(row=0, column=3)
    render(images[-1], canvas)
def importWindowyahia(root):
    newWindow = Toplevel(root)
    newWindow.geometry("1000x1000")
    def browse():
        global count


        filename = filedialog.askopenfilename(title="select File",
                                              filetypes = (("jpeg files","*.jpg"),("all files","*.*"),('png files', '*.png')))
        images.append(filename)
        canvas = Canvas(newWindow)
        canvas.config(width=1000, height=500)
        canvas.grid(row=1 , column=0,columnspan=3)
        img = ImageTk.PhotoImage(Image.open(images[0]))

        # images[0] = cv2.resize(images[0], (200, 200))

        filtering = tk.Button(newWindow, text="Add Filter", padx=90, pady=10, fg="white", bg="#2596be",
                              font=('arial', 15), command=lambda: image_filter(filename, canvas, newWindow))
        filtering.grid(row=0, column=1)

        test=canvas.create_image(0, 0, anchor="nw", image=img)
        test.grid(row=1 , column=0,columnspan=3)


        # mainloop()

    root.withdraw()
    root.geometry("500x500")
    newWindow.title("New Window")
    newWindow.geometry("500x500")
    browse_button = tk.Button(newWindow, text="Browse", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),command=browse)
    browse_button.grid(row=0 , column=0)


    ######## Back to previous window ########
    def on_closing():
        newWindow.destroy()
        root.deiconify()
    backButton = tk.Button(newWindow, text="Previous Page", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15), command=on_closing)
    backButton.grid(row=0 , column=2)

    newWindow.protocol("WM_DELETE_WINDOW", on_closing)



