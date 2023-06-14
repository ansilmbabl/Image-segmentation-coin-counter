# importing needed modules
import cv2
import cv2 as cv
import numpy as np
from module.preprocessing import preProcessing, empty
from module.window import window
from module.circle import DrawCircle

cap = cv.VideoCapture('http://192.168.1.72:8080/video')  # creating video capture object

# creating a trackbar window
window('edge', width=500, height=50)
cv.createTrackbar('start', 'edge', 50, 255, empty)
cv.createTrackbar('end', 'edge', 80, 250, empty)

# window('radius', width=500, height=50)
# min_radius = cv.createTrackbar('min', 'radius', 100, 1000, empty)
# max_radius = cv.createTrackbar('max', 'radius', 200, 1000, empty)

# capturing video (images) for detecting object using a while loop

one = 0
two = 0
five = 0
ten = 0

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img_pre = preProcessing(img, trackbar=False)
        window('pre processed', img_pre)  # preprocessed image
        # drawing circles
        img = DrawCircle(img,img_pre )
        window("webcam", img)


    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
