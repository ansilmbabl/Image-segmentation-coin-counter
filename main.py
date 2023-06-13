# importing needed modules
import cv2
import cv2 as cv
import numpy as np
from module.preprocessing import preProcessing, empty
from module.window import window
from module.circle import DrawCircle

cap = cv.VideoCapture("http://192.168.1.72:8080/video")  # creating video capture object

# creating a trackbar window
window('edge', width=500, height=50)
cv.createTrackbar('start', 'edge', 50, 255, empty)
cv.createTrackbar('end', 'edge', 100, 250, empty)

# window('radius', width=500, height=50)
# min_radius = cv.createTrackbar('min', 'radius', 100, 1000, empty)
# max_radius = cv.createTrackbar('max', 'radius', 1000, 1000, empty)

# capturing video (images) for detecting object using a while loop

one = 0
two = 0
five = 0
ten = 0

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img_pre = preProcessing(img, trackbar=True)
        window('edited', img_pre)  # preprocessed image
        # drawing circles
        circle, img = DrawCircle(img,img_pre)
        window("webcam", img)
        print(circle)
        cv.putText(img,"sdf",(100,100),cv.FONT_HERSHEY_SIMPLEX,5,(255,0,0),10)
        # for i in range(1, len(circle)+1 ):
        #     if 182<= circle['circle '+str(i)] <= 176:
        #         cv.putText(img,"10",(50,50),cv.FONT_HERSHEY_SIMPLEX,5,(255,255,0),3)
        #     elif 152<= circle['circle '+str(i)] <= 147:
        #         cv.putText(img,"5",(100,50),cv.FONT_HERSHEY_SIMPLEX,5,(255,255,0),3)
        #     elif 164<= circle['circle '+str(i)] <= 159:
        #         cv.putText(img,"2",(100,50),cv.FONT_HERSHEY_SIMPLEX,5,(255,255,0),3)
        #     elif 146<= circle['circle '+str(i)] <= 140:
        #         cv.putText(img,"1",(100,50),cv.FONT_HERSHEY_SIMPLEX,5,(255,255,0),3)

    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
