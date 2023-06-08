# importing needed modules
import cv2
import cv2 as cv
import numpy as np
from module.preprocessing import preProcessing, empty

cap = cv.VideoCapture(0)  # creating video capture object
cap.set(3, 640)  # setting width of frame
cap.set(4, 480)  # setting height of frame


# creating a trackbar window
cv.namedWindow("edge")
cv.createTrackbar('start', 'edge', 50, 255, empty)
cv.createTrackbar('end', 'edge', 100, 250, empty)


# capturing video (images) for detecting object using a while loop
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img_pre = preProcessing(img, trackbar=True)
        cv.imshow('edited', img_pre)  # preprocessed image
        cnt, hir = cv.findContours(img_pre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cv.imshow("cnt", cnt)
        cv.imshow("window", img)
    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
