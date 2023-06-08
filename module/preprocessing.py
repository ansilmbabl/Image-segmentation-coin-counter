import cv2
import cv2 as cv
import numpy as np


def empty(a):
    pass


def preProcessing(img, trackbar=False):
    """
    returns pre-processed image which include Gaussian blurring, Canny edge detection, dilation steps

    :param img: image to be processed
    :param trackbar: trackbar position to set canny edge detection thresholds
    :return: pre-processed image
    """

    img = cv.GaussianBlur(img, (5, 5), 10)
    if trackbar:
        start = cv.getTrackbarPos('start', 'edge')
        end = cv.getTrackbarPos('end', 'edge')
        img = cv.Canny(img, start, end)
    else:
        img = cv.Canny(img, 50, 250)
    kernel = np.ones((3, 3), np.uint8)  # kernel for dilation
    img = cv.dilate(img, kernel, iterations=1)
    img = cv.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return img
