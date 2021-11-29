import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
# from tkinter import *
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import time
import cv2
from Tkinter.GUI_Live import camera
# from snapshot import App, videoCapture
root = tk.Tk()
images = []
from GUI_Image import importWindowyahia


######### import Window ##########

def importWindow():
    importWindowyahia(root)

########### second-window #############

def videoWindow():
    cameraWindow = Toplevel(root)
    root.withdraw()
    cameraWindow.title("New Window")
    cameraWindow.geometry("700x700")
    Label(cameraWindow,
          text="This is a new window").grid()

    camera(cameraWindow)


    ######## Back to previous window ########
    def on_closing():
        cameraWindow.destroy()
        root.deiconify()
    backButton = tk.Button(cameraWindow, text="Previous Page", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15), command=on_closing)
    backButton.grid()

    cameraWindow.protocol("WM_DELETE_WINDOW", on_closing)



########## Home-Page ##########
image= PhotoImage(file ='../assest/image.png',width=700,height=700)
Label(root, image= image, bg="black",).grid(column=0,row=0,columnspan=2)

importButton = tk.Button(text="Import", padx=90, pady=10, fg="white", bg="#2596be", font=('arial',15), command=importWindow)
importButton.grid(row=1,column=0)


cameraButton= tk.Button(text="Camera", padx=90, pady=10, fg="white", bg="#2596be",font=('arial',15), command=videoWindow)
cameraButton.grid(row=1,column=1)


###########################################
root.mainloop()