import cv2 as cv


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
    img = cv.dilate(img, (25, 25))
    return img
