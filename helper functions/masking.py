import cv2 as cv
import numpy as np

# creating video capture object
cap = cv.VideoCapture(0)


def empty(a):  # function used as the parameter for cv.createTrackbar
    pass


# creating window for setting hsv values by trackbar
cv.namedWindow('hsv', cv.WINDOW_NORMAL)
cv.resizeWindow('hsv', 640, 360)
cv.createTrackbar('lower_h', 'hsv', 0, 255, empty)
cv.createTrackbar('higher_h', 'hsv', 255, 255, empty)
cv.createTrackbar('lower_s', 'hsv', 0, 255, empty)
cv.createTrackbar('higher_s', 'hsv', 255, 255, empty)
cv.createTrackbar('lower_v', 'hsv', 0, 255, empty)
cv.createTrackbar('higher_v', 'hsv', 255, 255, empty)


# capturing continuous images
while cap.isOpened():
    # reading current frame
    ret, image = cap.read()

    # converting image to hsv
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # finding lower bound and upper bound
    l_h = cv.getTrackbarPos('lower_h', 'hsv')
    h_h = cv.getTrackbarPos('higher_h', 'hsv')
    l_s = cv.getTrackbarPos('lower_s', 'hsv')
    h_s = cv.getTrackbarPos('higher_s', 'hsv')
    l_v = cv.getTrackbarPos('lower_v', 'hsv')
    h_v = cv.getTrackbarPos('higher_v', 'hsv')
    lower_hsv = np.array([l_h, l_s, l_v])
    higher_hsv = np.array([h_h, h_s, h_v])

    print(lower_hsv, higher_hsv)

    # masking the image
    mask = cv.inRange(hsv, lower_hsv, higher_hsv)
    res = cv.bitwise_and(image, image, mask=mask)

    # displaying results
    cv.imshow('out', image)  # output image
    cv.imshow('mask',mask)  # mask applied
    cv.imshow('res',res)  # output after applying mask

    # exit the loop by pressing 'q'
    if cv.waitKey(1) == ord('q'):
        break

# release video capture object
cap.release()
cv.destroyAllWindows()

