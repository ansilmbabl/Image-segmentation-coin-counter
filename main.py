# importing needed modules
import cv2
import cv2 as cv
import numpy as np
from module.preprocessing import preProcessing, empty
from module.window import window

cap = cv.VideoCapture("http://192.168.1.72:8080/video")  # creating video capture object

# creating a trackbar window
window('edge', width=500, height=50)
cv.createTrackbar('start', 'edge', 50, 255, empty)
cv.createTrackbar('end', 'edge', 100, 250, empty)

# capturing video (images) for detecting object using a while loop
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img_pre = preProcessing(img, trackbar=True)
        window('edited', img_pre)  # preprocessed image
        # drawing circles
        circles = cv.HoughCircles(img_pre, cv2.HOUGH_GRADIENT, dp=1, minDist=90, param1=50, param2=30, minRadius=100, maxRadius=200)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0,:]:
                center = (circle[0],circle[1])
                radius = circle[2]
                cv.circle(img,center,radius,(0,0,255),3)
        cv.imshow("webcam", img)
    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
