"""
We can use this file to get the hsv vales of a color (blue,green,red)

"""

import numpy as np
import cv2 as cv

b, g, r = 172, 146, 133
bgr = np.uint8([[[b, g, r]]])
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
print(hsv)
