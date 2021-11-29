import tkinter as tk
from PIL import ImageTk, Image
import cv2
from filters_live.video_filtering_face import video_filtering_face,change_filter
from tkinter import Tk
from tkinter.ttk import Frame, Label
from background_live.request_image import add_path,check_image

save = False
count_filter = 0
count_back = 1
show_filter_live = False
show_background_live = False

def camera(newWindow):
    app = Frame(newWindow)
    app.grid()
    lmain = Label(app)
    lmain.grid()



    def printInput():
        add_path(inputtxt2.get(1.0, "end-1c"))

    inputtxt2 = tk.Text(newWindow,
                       height=5,
                       width=20)
    inputtxt2.grid(row=0, column=1)
    printButton = tk.Button(newWindow,
                            text = "Print",
                            command = printInput)
    printButton.grid(row=0, column=1)

    def nextback():
        global count_back,show_background_live
        len_image = check_image()
        if count_back == len_image:
            show_background_live = False
            count_back=1
        else:
            show_background_live = True
            count_back+=1
    def nextWindow():
         global count_filter,show_filter_live
         if count_filter == len(change_filter)-1:
             show_filter_live = False
             count_filter= -1
         else:
             show_filter_live = True
             count_filter+=1

    def saveWindow():
        global save
        save =True


    importButton = tk.Button(newWindow,text="Next background", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
                             command=nextback)
    importButton.grid(row=1, column=0)
    importButton = tk.Button(newWindow,text="Next filter", padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
                             command=nextWindow)
    importButton.grid(row=1, column=1)
    importButton = tk.Button(newWindow,text='capture and save', padx=90, pady=10, fg="white", bg="#2596be", font=('arial', 15),
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

    def print_path2(inputtxt, frame):
        name = inputtxt.get(1.0, "end-1c")
        print(name)
        img_name = f"../saved/{name}.png"
        cv2.imwrite(img_name, frame)
    def path_name(frame):

        inputtxt = tk.Text(newWindow,
                           height=5,
                           width=20)

        inputtxt.grid(row=1, column=2)

        printButton = tk.Button(newWindow,
                                text="save image",
                                command=lambda: print_path2(inputtxt, frame))
        printButton.grid(row=1, column=2)




    video_stream3()

# newWindow.mainloop()


