from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import sys
import cv2
from PIL import Image
import sys
import numpy as np


def thug_mask(image):
    maskpath = "mask.png"
    cascPath = "haarcascade_frontalface_default.xml"
    mask = Image.open(maskpath)

    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.fromarray(image)

    for (x, y, w, h) in faces:
        resized_mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(resized_mask, offset, mask=resized_mask)

    return np.asarray(background)


class MainApp(App):
    def build(self):
        button = Button(text = 'Click here',size_hint= (0.2,0.2),font_size = '20sp', pos_hint = {'center_x':0.5, 'center_y':0.5},on_press = self.kivi)

        return  button


    def kivi(self, obj):
        print("it is ok")

        cap = cv2.VideoCapture(0)

        while (True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', thug_mask(frame))
            if cv2.waitKey(1) & 0xfFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()



MainApp().run()