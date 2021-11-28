import cv2
import mediapipe as mp
import numpy as np
from request_image import add_path
def background(path,blur =1,img=2):
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    back1=1
    cam = cv2.VideoCapture(0)
    cam.set(3, 1280)
    cam.set(4, 720)
    fsize = (520, 720)



    # begin with selfie segmentation model


    while cam.isOpened():
        scene = cv2.imread(path)  # read the scene image
        scene = cv2.blur(scene, (1, 1))
        scene = cv2.resize(scene, (fsize[1], fsize[0]))  # resize scene to the size of frame
        with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_seg:
            bg_image = scene
            ret, frame = cam.read()
            if not ret:
                print("Error reading frame...")
                continue
            frame = cv2.resize(frame, (fsize[1], fsize[0]))

            # flip it to look like selfie camera
            frame = cv2.flip(frame, 1)

            # get rgb image to pass that on selfie segmentation
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # process it!
            results = selfie_seg.process(rgb)

            # get the condition from result's segmentation mask
            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1

            # apply background change if condition matches
            output_image = np.where(condition, frame, bg_image)

            # show the output
            cv2.imshow('Background Change with MP', output_image)
            key = cv2.waitKey(5) & 0xFF

            if key == ord('n'):
                back1+=1
                if back1 ==img+1:
                    back1=1
                path = f'../assest/background/back{back1}.png'


            if key == ord('q'):
                cam.release()
                cv2.destroyAllWindows()  # wait until any key is pressed
    cam.release()
    cv2.destroyAllWindows()



