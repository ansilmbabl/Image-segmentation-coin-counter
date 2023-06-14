import cv2 as cv
import numpy as np
from module.window import window


def coin(radius, image):
    if radius >= 190:
        cv.putText(image, "10", (50, 100), cv.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 3)
    elif 177 >= radius >= 170:
        cv.putText(image, "5", (50, 300), cv.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 3)
    elif 186 >= radius >= 179:
        cv.putText(image, "2", (50, 500), cv.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 3)
    elif 165 >= radius >= 150:
        cv.putText(image, "1", (50, 700), cv.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 3)


def DrawCircle(image, preprocess_image, dp=0.2, minDist=80, param1=50, param2=30, minRadius=100,
               maxRadius=200):
    # global center
    circles = cv.HoughCircles(preprocess_image, cv.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2,
                              minRadius=minRadius,
                              maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        l =[]
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv.circle(image, center, radius, (0, 255, 0), 3)
            coin(radius, image)
            l.append(radius)
        print(max(l),min(l))
        return image
