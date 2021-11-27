import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
# from tkinter import *
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import time
import cv2
from snapshot import App, videoCapture
root = tk.Tk()
images = []


######### import Window ##########
def importWindow():
    def browse(newWindow):
        filename = filedialog.askopenfilename(initialdir="/home/yousef/Pictures", title="select File",
                                              filetypes=(("executables", "*.jpg"), ("all files", "*.*")))
        images.append(filename)

        canv = Canvas(newWindow, width=150, height=150, bg='white')
        canv.grid(row=2, column=3)

        img = ImageTk.PhotoImage(Image.open('Cat03.jpg'))
        canv.create_image(20, 20, anchor=NW, image=img)


    newWindow = Toplevel(root)
    root.withdraw()
    newWindow.title("New Window")
    newWindow.geometry("700x700")
    Label(newWindow,
          text="This is a new window").grid()
    backButton = tk.Button(newWindow, text="Browse", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),command=lambda: browse(newWindow))
    backButton.grid()

    ######## Back to previous window ########
    def on_closing():
        newWindow.destroy()
        root.deiconify()
    backButton = tk.Button(newWindow, text="Previous Page", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15), command=on_closing)
    backButton.grid()

    newWindow.protocol("WM_DELETE_WINDOW", on_closing)



########### second-window #############

def videoWindow():
    def openCamera():
        # cap=cv2.VideoCapture(0)
        # frame=cap.read()
        # cv2.imshow('frame', frame)
        # cv2.waitKey(0)
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(1)


        canv = Canvas(newWindow, width=150, height=150, bg='white')
        canv.grid(row=2, column=3)


        img = ImageTk.PhotoImage(Image.open('Cat03.jpg'))
        canv.create_image(20, 20, anchor=NW, image=img)


    newWindow = Toplevel(root)
    root.withdraw()
    newWindow.title("New Window")
    newWindow.geometry("700x700")
    Label(newWindow,
          text="This is a new window").grid()
    backButton = tk.Button(newWindow, text="Browse", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15), command=openCamera)
    backButton.grid()




    ######## Back to previous window ########
    def on_closing():
        newWindow.destroy()
        root.deiconify()
    backButton = tk.Button(newWindow, text="Previous Page", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15), command=on_closing)
    backButton.grid()

    newWindow.protocol("WM_DELETE_WINDOW", on_closing)



########## Home-Page ##########
image= PhotoImage(file ='../assest/image.png',width=700,height=700)
Label(root, image= image, bg="black",).grid(column=0,row=0,columnspan=2)

importButton = tk.Button(text="Import", padx=90, pady=10, fg="white", bg="#2596be", font=('arial',15), command=importWindow)
importButton.grid(row=1,column=0)


cameraButton= tk.Button(text="Camera", padx=90, pady=10, fg="white", bg="#2596be",font=('arial',15), command=videoWindow)
cameraButton.grid(row=1,column=1)


###########################################
root.mainloop()





