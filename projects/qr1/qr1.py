import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pyzbar.pyzbar import decode
print("Enter 0 if you want to upload image", "Enter 1 if you want to use camera", sep=' || ')
x=input()
if x=='0':
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    img = cv2.imread(filename)
    for qrcode in decode(img):
	    myData = qrcode.data.decode('utf-8')
	    print(myData)
elif x=='1':
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        success, img = cap.read()
        for qrcode in decode(img):
            myData = qrcode.data.decode('utf-8')
            print(myData)
            pts = np.array([qrcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(0,255,0),5)
            pts2 = qrcode.rect
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)

        cv2.imshow('Result',img)
        cv2.waitKey(1)
        #cv2.destroyAllWindows()
else:
    print("ERROR")


