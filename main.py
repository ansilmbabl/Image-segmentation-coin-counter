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
        # finding contours
        cnt, hir = cv.findContours(img_pre, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(cnt))

        # drawing bounding rectangle
        for i in cnt:
            if 20 >= len(cnt) >= 8:
                cv.drawContours(img, cnt, -1, (0, 255, 0), 3)
                x, y, w, h = cv.boundingRect(i)
                cv.rectangle(img_pre, (x, y), (x + w, y + h), (255, 0, 0), 4)

        cv.imshow("cnt", img_pre)
        cv.imshow("window", img)
    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
