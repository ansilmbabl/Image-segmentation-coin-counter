import cv2 as cv
import numpy as np

# creating video capture object
cap = cv.VideoCapture(0)


def empty(a):  # function used as the parameter for cv.createTrackbar
    pass


cv.namedWindow('canny', cv.WINDOW_NORMAL)
cv.resizeWindow('canny', 500, 50)
cv.createTrackbar('st', 'canny', 0, 255, empty)
cv.createTrackbar('en', 'canny', 100, 255, empty)

while cap.isOpened():
    # reading current frame
    ret, image = cap.read()

    # converting to grayscale
    grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Gaussian blur to reduce noise
    blur = cv.GaussianBlur(grey, (5, 5), 5)

    # canny edge detection
    t1, t2 = cv.getTrackbarPos('st', 'canny'), cv.getTrackbarPos('en', 'canny')
    canny = cv.Canny(blur, t1, t2)
    print(t1,t2)

    # applying some morphological operations
    kernel = np.ones((3, 3), np.uint8)  # kernel for dilation
    img = cv.dilate(canny, kernel, iterations=2)
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

    # displaying result
    cv.imshow('out', image)  # output image
    cv.imshow('result', img)  # canny edge

    # exit the loop by pressing 'q'
    if cv.waitKey(1) == ord('q'):
        break

# release video capture object
cap.release()
cv.destroyAllWindows()