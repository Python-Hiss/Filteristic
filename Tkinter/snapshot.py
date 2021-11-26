from tkinter import *
import cv2
from PIL import Image, ImageTk
import time
# root = Tk()
# from GUI import *

class App:
    def __init__(self, video_source=0):
        self.appName = "Filtiristic v1.0"
        self.window = Tk()
        self.window.title(self.appName)
        self.window.resizable(0, 0)
        # self.window.wm_iconbitmap("cam.ico")
        self.window["bg"] = "black"
        self.video_source = video_source

        self.vid = videoCapture(self.video_source)
        self.label = Label(self.window, text=self.appName, font=15, bg="blue", fg="white").pack(side=TOP, fill=BOTH)

        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height, bg="red")
        self.canvas.pack()

        self.btn_snapshot = Button(self.window, text="capture", width=30, bg="white", activebackground="red",
                                   command=self.snapshot)
        self.btn_snapshot.pack(anchor=CENTER, expand=True)
        self.update()
        self.window.mainloop()

    def snapshot(self):
            check, frame = self.vid.getFrame()
            if check:
                image = "IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
                cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                msg = Label(self.window, text="image saved"+image,bg="black", fg="green").place(x=430, y=510)

    def update(self):
        isTrue, frame = self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(15, self.update)





########### Class for Capture Video##############3
class videoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("error video")

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
        else:
            return None

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()




if __name__ == "__main__":
    App()
