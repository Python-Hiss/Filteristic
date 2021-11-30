import tkinter as tk
from PIL import ImageTk, Image
import cv2
from filters_live.video_filtering_face import video_filtering_face,change_filter
from tkinter_custom_button import TkinterCustomButton
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
    app.pack()
    lmain = Label(app)
    lmain.pack()

    def printInput():
        add_path(inputtxt2.get(1.0, "end-1c"))

    inputtxt2 = tk.Text(newWindow,
                       height=1,
                       width=20)
    inputtxt2.place(x=400,y=550)
    printButton = TkinterCustomButton(master=newWindow,text="Add New Background", corner_radius=5, command=printInput, fg_color="#3319CB", hover_color="#005DFE",
                        width=150,
                        cursor="shuttle", text_font=("sans-serif", 10))
    printButton.place(x=408,y=570)

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

    # def saveWindow():



    importButton = TkinterCustomButton(master=newWindow,text="Next background", corner_radius=5, command=nextback, fg_color="#3319CB", hover_color="#005DFE",
                        width=300,
                        cursor="shuttle", text_font=("sans-serif", 20))
    importButton.place(x=500,y=490)
    importButton = TkinterCustomButton(master=newWindow,text="Next filter", corner_radius=5, command=nextWindow, fg_color="#3319CB", hover_color="#005DFE",
                        width=300, cursor="shuttle", text_font=("sans-serif", 20))
    importButton.place(x=160,y=490)
    image = tk.PhotoImage(file='../assest/camera.png')
    importButton = TkinterCustomButton(master=newWindow, corner_radius=20,
                                       command=lambda:open_popup(newWindow), fg_color="#f1f1f1", hover_color="#c1c1c1", cursor="shuttle",
                                       image=image,
                                       width=50)
    importButton.place(x=740,y=431)

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
        inputtxt.pack()
        printButton = TkinterCustomButton(master=newWindow,text="Save Image", corner_radius=5, command=lambda: print_path2(inputtxt, frame), fg_color="#3319CB",
                            hover_color="#005DFE", width=300,
                            cursor="shuttle", text_font=("sans-serif", 20))
        printButton.pack()
    newWindow.geometry("960x630")
    newWindow.bind("<Right>", lambda x: nextWindow())
    newWindow.bind("<Left>", lambda x: nextback())
    video_stream3()
    def open_popup(newWindow):
        top = tk.Toplevel(newWindow)
        top.geometry("250x150")
        top.title("save")
        global save
        save = True

# newWindow.mainloop()


