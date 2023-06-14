import cv2 as cv
import numpy as np

cap = cv.VideoCapture('http://192.168.1.72:8080/video')
cv.namedWindow('out', cv.WINDOW_NORMAL)
cv.resizeWindow('out', 640, 360)


def pas(a):
    pass

cv.namedWindow('canny',cv.WINDOW_NORMAL)
cv.resizeWindow('canny',640,360)
cv.createTrackbar('st','canny',50,255,pas)
cv.createTrackbar('en','canny',240,255,pas)

# cv.namedWindow('hsv', cv.WINDOW_NORMAL)
# cv.resizeWindow('hsv', 640, 360)
# cv.createTrackbar('lower_h', 'hsv', 0, 255, pas)
# cv.createTrackbar('higher_h', 'hsv', 255, 255, pas)
# cv.createTrackbar('lower_s', 'hsv', 0, 255, pas)
# cv.createTrackbar('higher_s', 'hsv', 255, 255, pas)
# cv.createTrackbar('lower_v', 'hsv', 0, 255, pas)
# cv.createTrackbar('higher_v', 'hsv', 255, 255, pas)

while cap.isOpened():
    ret, image = cap.read()

    t1,t2 = cv.getTrackbarPos('st', 'canny'), cv.getTrackbarPos('en', 'canny')
    grey = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grey,(5,5),5)
    canny = cv.Canny(blur,t1,t2)
    kernel = np.ones((3, 3), np.uint8)  # kernel for dilation
    img = cv.dilate(canny, kernel, iterations=2)
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i,contour in enumerate(contours):
        area = cv.contourArea(contour)
        perimeter = cv.arcLength(contour, closed=True)

        epsilon = perimeter * 0.02
        approx = cv.approxPolyDP(contour,epsilon,closed=True)

        x,y,w,h = cv.boundingRect(approx)
        cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
        cv.circle(image,(x+w//2,y+h//2),(w//2),(0,255,0),5)

        roi = image[y:y+h,x:x+w]
        if roi is not None:
            hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
            cv.imshow('contour' + str(i), hsv_roi)

    # hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # l_h = cv.getTrackbarPos('lower_h', 'hsv')
    # h_h = cv.getTrackbarPos('higher_h', 'hsv')
    # l_s = cv.getTrackbarPos('lower_s', 'hsv')
    # h_s = cv.getTrackbarPos('higher_s', 'hsv')
    # l_v = cv.getTrackbarPos('lower_v', 'hsv')
    # h_v = cv.getTrackbarPos('higher_v', 'hsv')
    #
    # lower_hsv = np.array([l_h, l_s, l_v])
    # higher_hsv = np.array([h_h, h_s, h_v])
    #
    # print(lower_hsv,higher_hsv)
    #
    # mask = cv.inRange(hsv, lower_hsv, higher_hsv)
    # res = cv.bitwise_and(image, image, mask=mask)

    # cv.imshow('hsvimage', hsv)
    # cv.imshow('res', res)
    # cv.imshow('mask', mask)
    cv.imshow('out', image)
    # cv.imshow('canny', img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
