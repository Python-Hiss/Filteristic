import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
import cv2
from filters_live.video_filtering_face import video_filtering_face,change_filter,background
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
# from background_live.background_live import  background
from background_live.request_image import add_path,check_image
root = Tk()
# Create a frame
app = Frame(root)
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()

# i=0
# save =False
#
# def nextWindow():
#      global i
#      if i == len(change_filter)-1:
#          i=-1
#      i+=1
#
#
# def saveWindow():
#     global save
#     save =True
#     # frame= video_stream
#     # print(type(frame))
#     # img_name = "../saved/opencv_frame.png"
#     # cv2.imwrite(img_name, frame)
#     # frames = cv2.imread(img_name)
#     # cv2.imshow("Frame", frames)
#     # key = cv2.waitKey(0)
#
# importButton = tk.Button(text="Next", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
#                          command=nextWindow)
# importButton.grid(row=1, column=0)
# if not save :
# importButton = tk.Button(text='capture and save', padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
#                          command=saveWindow)
# importButton.grid(row=2, column=0)
#
#
# def video_stream():
#
#     frame = video_filtering_face(
#         change_filter[i]['filter'],
#         change_filter[i]['center'],
#         change_filter[i]['width'],
#         change_filter[i]['height'],
#         change_filter[i]['up'],
#         change_filter[i]['left'],
#         change_filter[i]['counte']
#     )
#
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     if save:
#         save_image(frame)
#
#     lmain.after(1, video_stream)
#
#
# def save_image(frame):
#     global save
#     save = False
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     name = input('save name')
#     img_name = f"../saved/{name}.png"
#     cv2.imwrite(img_name, frame)
#
#


# video_stream()


# def nextback():
#     global var
#     len_image = check_image()
#     if var == len_image:
#         var=1
#
#     var+=1
# importButton = tk.Button(text="Next", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
#                          command=nextback)
# importButton.grid(row=1, column=0)
# def video_stream2():
#
#     frame = background(f'../assest/background/back{var}.png',1,6)
#
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     if save:
#         save_image(frame)
#
#     lmain.after(1, video_stream2)
# def save_image(frame):
#     global save
#     save = False
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     name = input('save name')
#     img_name = f"../saved/{name}.png"
#     cv2.imwrite(img_name, frame)
# video_stream2()

def printInput():
    add_path(inputtxt2.get(1.0, "end-1c"))

#
#
inputtxt2 = tk.Text(root,
                   height=5,
                   width=20)
inputtxt2.grid(row=0, column=1)
printButton = tk.Button(root,
                        text = "Print",
                        command = printInput)
printButton.grid(row=0, column=1)


save =False
count_filter=0
count_back=1
show_filter_live =True
show_background_live =True
def nextback():
    global var,show_background_live
    len_image = check_image()
    if var == len_image:
        show_background_live = False
        var=1
    else:
        show_background_live = True
        var+=1
def nextWindow():
     global i,show_filter_live
     if i == len(change_filter)-1:
         show_filter_live = False
         i= -1
     else:
         show_filter_live = True
         i+=1

def saveWindow():
    global save
    save =True




importButton = tk.Button(text="Next background", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
                         command=nextback)
importButton.grid(row=1, column=0)
importButton = tk.Button(text="Next filter", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
                         command=nextWindow)
importButton.grid(row=1, column=1)
importButton = tk.Button(text='capture and save', padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
                         command=saveWindow)
importButton.grid(row=2, column=0)

def video_stream3():

    frame = video_filtering_face(
        change_filter[count_filter]['filter'],
        change_filter[count_filter]['center'],
        change_filter[count_filter]['width'],
        change_filter[count_filter]['height'],
        change_filter[count_filter]['up'],
        change_filter[count_filter]['left'],
        f'../assest/background/back{count_back}.png',
        1,show_filter_live,show_background_live

    )

    cv2image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img2 = Image.fromarray(cv2image2)
    imgtk2 = ImageTk.PhotoImage(image=img2)
    lmain.imgtk = imgtk2
    lmain.configure(image=imgtk2)
    if save:
        save_image(frame)
    lmain.after(1, video_stream3)
def save_image(frame):
    global save
    save = False
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    path_name(frame)

def path_name(frame):
    global print_path
    inputtxt = tk.Text(root,
                       height=5,
                       width=20)

    inputtxt.grid(row=0, column=1)

    printButton = tk.Button(root,
                            text="Print",
                            command=lambda: print_path(inputtxt, frame))
    printButton.grid(row=0, column=1)

def print_path(inputtxt, frame):
    name = inputtxt.get(1.0, "end-1c")
    img_name = f"../saved/{name}.png"
    cv2.imwrite(img_name, frame)


video_stream3()

root.mainloop()


