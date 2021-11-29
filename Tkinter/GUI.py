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
from tkinter_custom_button import TkinterCustomButton

# from snapshot import App, videoCapture
root = tk.Tk()
images = []
from Tkinter.GUI_Image import importWindowyahia


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
root.geometry("960x630")
image= PhotoImage(file ='../assest/2.png',width=960,height=540)
Label(root, image= image).grid(column=0,row=0,columnspan=2)
Label().grid(column=0,row=1)
importButton =TkinterCustomButton(text="Image", corner_radius=5, command=importWindow,fg_color="#3319CB",hover_color="#005DFE",width=300,
                                  cursor="shuttle",text_font=("sans-serif", 20))
importButton.grid(row=2,column=0)
Label().grid(column=1,row=1)
cameraButton= TkinterCustomButton(text="Camera", corner_radius=5, command=videoWindow,fg_color="#3319CB",hover_color="#005DFE",width=300,
                                  cursor="shuttle",text_font=("sans-serif", 20))
# cameraButton.place(relx=0.5, rely=0.5, anchor=CENTER)
cameraButton.grid(row=2,column=1)


###########################################
root.mainloop()