import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
# from tkinter import *
from main import cap
from PIL import Image

root = tk.Tk()
images = []

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/home/yousef", title="select File", filetypes=(("executables","*.png"), ("all files","*.*")))
    images.append(filename)
    for img in images:
        label = tk.Label(frame, text=img, bg="gray")
        label.pack()

def runApps():
    for img in images:
        if sys.platform=="win32":
         os.startfile(img)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, img])

canvas = tk.Canvas(root, width=1000,heigh=800,bg ="#2596be")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile= tk.Button(text="Browse", padx=18, pady=5, fg="white", bg="#2596be", command=addApp)
openFile.pack(side=tk.BOTTOM)

secondButton= tk.Button(text="Run App", padx=18, pady=5, fg="white", bg="#2596be", command=runApps)
secondButton.pack(side=tk.BOTTOM)



root.mainloop()



