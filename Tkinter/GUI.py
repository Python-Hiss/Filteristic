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
from GUI_background import background_window

# from snapshot import App, videoCapture
root = tk.Tk()
images = []
from Tkinter.GUI_Image import importWindowyahia


######### filter image Window ##########

def importFilterWindow(new):
    importWindowyahia(new)

######### background image Window ##########

def backgroundWindow(new):
    background_window(new)

######### import Window ##########

def importWindow():
    importWindow = Toplevel(root)
    root.withdraw()
    importWindow.title("Import Window")
    importWindow.geometry("700x400")
    Label(importWindow, text="", font=("Arial", 50)).pack()
    Label(importWindow,text="Editing Type", font=("Arial", 25)).pack()
    Label(importWindow, text="", font=("Arial", 25)).pack()

    filterButton = TkinterCustomButton(master =importWindow, text="Add Filter", corner_radius=5, command= lambda: importFilterWindow(importWindow),
                                       fg_color="#FF5C58", hover_color="#ff544f", width=300,
                                    cursor="shuttle", text_font=("sans-serif", 20))
    filterButton.pack()

    Label(importWindow, text="", font=("Arial", 25)).pack()

    backgroundButton = TkinterCustomButton(master=importWindow, text="Add Background", corner_radius=5, command=lambda: backgroundWindow(importWindow),
                                           fg_color="#FF5C58", hover_color="#ff544f", width=300,
                                       cursor="shuttle", text_font=("sans-serif", 20))

    backgroundButton.pack()

    def on_closing():
        importWindow.destroy()
        root.deiconify()

    importWindow.protocol("WM_DELETE_WINDOW", on_closing)

    image = PhotoImage(file='../assest/back.png')
    backButton = TkinterCustomButton(master=importWindow, corner_radius=15,
                                     command=on_closing, fg_color="#f1f1f1", hover_color="#c1c1c1", cursor="shuttle",
                                     image=image, width=50)

    backButton.place(x=0, y=3)

########### second-window #############

def videoWindow():
    cameraWindow = Toplevel(root)
    root.withdraw()
    cameraWindow.title("New Window")
    # cameraWindow.geometry("700x700")
    camera(cameraWindow)


    ######## Back to previous window ########
    def on_closing():
        cameraWindow.destroy()
        root.deiconify()

    image= PhotoImage(file ='../assest/back.png')
    backButton = TkinterCustomButton(master=cameraWindow, corner_radius=15,
                        command=on_closing, fg_color="#f1f1f1", hover_color="#c1c1c1", cursor="shuttle", image=image,
                        width=50)
    backButton.place(x=0,y=3)


    cameraWindow.protocol("WM_DELETE_WINDOW", on_closing)



########## Home-Page ##########
root.geometry("960x630")
image= PhotoImage(file ='../assest/2.png',width=960,height=540)
Label(root, image= image).grid(column=0,row=0,columnspan=2)
Label().grid(column=0,row=1)
importButton =TkinterCustomButton(text="Image", corner_radius=5, command=importWindow,fg_color="#FF5C58",hover_color="#ff544f",width=300,
                                  cursor="shuttle",text_font=("sans-serif", 20))
importButton.grid(row=2,column=0)
Label().grid(column=1,row=1)
cameraButton= TkinterCustomButton(text="Camera", corner_radius=5, command=videoWindow,fg_color="#FF5C58",hover_color="#ff544f",width=300,
                                  cursor="shuttle",text_font=("sans-serif", 20))
# cameraButton.place(relx=0.5, rely=0.5, anchor=CENTER)
cameraButton.grid(row=2,column=1)


###########################################
root.mainloop()