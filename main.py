# importing needed modules
import cv2
import cv2 as cv
import numpy as np
from module.preprocessing import preProcessing, empty
from module.window import window


cap = cv.VideoCapture("http://192.168.1.72:8080/video")  # creating video capture object

# creating a trackbar window
window('edge',width=500,height=50)
cv.createTrackbar('start', 'edge', 50, 255, empty)
cv.createTrackbar('end', 'edge', 100, 250, empty)

# capturing video (images) for detecting object using a while loop
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img_pre = preProcessing(img, trackbar=True)
        window('edited', img_pre)  # preprocessed image
        # finding contours
        cnt, hir = cv.findContours(img_pre, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(cnt))

        # drawing bounding rectangle
        for i in cnt:
              if 90 >= len(cnt) >= 180:
                # contour_perimeter = cv.arcLength(cnt,closed=True)
                # print(contour_perimeter)
                # contour_area = cv.contourArea(cnt)
                cv.drawContours(img, cnt, -1, (0, 255, 0), 3)
                x, y, w, h = cv.boundingRect(i)
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)

        window("cnt", img_pre)
        window("webcam", img)
    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
