import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
# from tkinter import *

# from PIL import Image

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
canvas = tk.Canvas(root, width=1000,height=800,bg ="#2596be")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile= tk.Button(text="Browse", padx=18, pady=5, fg="white", bg="#2596be", command=addApp)
openFile.pack(side=tk.BOTTOM)

secondButton= tk.Button(text="Run App", padx=18, pady=5, fg="white", bg="#2596be", command=runApps)
secondButton.pack(side=tk.BOTTOM)



root.mainloop()

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from PIL import Image, ImageTk


# class Root(Tk):
#     def __init__(self):
#         super(Root, self).__init__()
#         self.title("Python Tkinter Dialog Widget")
#         self.minsize(640, 400)

#         self.labelFrame = ttk.LabelFrame(self, text = "Open File")
#         self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

#         self.button()


#     def button(self):
#         self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
#         self.button.grid(column = 1, row = 1)


#     def fileDialog(self):

#         self.filename = filedialog.askopenfilename(initialdir="/home", title = "Select A File", filetype =
#         (("jpeg files","*.jpg"),("all files","*.*")) )
#         self.label = ttk.Label(self.labelFrame, text = "")
#         self.label.grid(column = 1, row = 2)
#         self.label.configure(text = self.filename)

#         img = Image.open(self.filename)
#         photo = ImageTk.PhotoImage(img)

#         self.label2 = Label(image=photo)
#         self.label2.image = photo
#         self.label2.grid(column=3, row=4)

# root = Root()
# root.mainloop()


