import cv2 as cv
import numpy as np
from module.window import window


def DrawCircle(image, preprocess_image, dp=1, minDist=90, param1=50, param2=30, minRadius=100,
               maxRadius=200):
    # global center
    circles = cv.HoughCircles(preprocess_image, cv.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2,
                              minRadius=minRadius,
                              maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        radii = {}
        count = 1
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            image = cv.circle(image, center, radius, (0, 0, 255), 3)
            radii['circle ' + str(count)] = radius
            count += 1
        return radii,image
