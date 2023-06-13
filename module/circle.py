import cv2 as cv
import numpy as np
from module.window import window


def DrawCircle(image, preprocess_image, dp=1, minDist=90, param1=50, param2=30, minRadius=100,
               maxRadius=200):
    circles = cv.HoughCircles(preprocess_image, cv.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2,
                              minRadius=minRadius,
                              maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv.circle(image, center, radius, (0, 0, 255), 3)
            window("webcam", image)
