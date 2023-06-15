import cv2 as cv
import numpy as np

# creating video capture object (ip webcam)
cap = cv.VideoCapture('http://192.168.1.71:8080/video')
# resizing the output window
cv.namedWindow('out', cv.WINDOW_NORMAL)
cv.resizeWindow('out', 640, 360)


def empty(a):  # function used as the parameter for cv.createTrackbar
    pass


# creating window for setting Canny thresholds by trackbar
cv.namedWindow('canny', cv.WINDOW_NORMAL)
cv.resizeWindow('canny', 500, 50)
cv.createTrackbar('st', 'canny', 46, 255, empty)
cv.createTrackbar('en', 'canny', 255, 255, empty)

# # creating window for setting hsv values by trackbar
# cv.namedWindow('hsv', cv.WINDOW_NORMAL)
# cv.resizeWindow('hsv', 640, 360)
# cv.createTrackbar('lower_h', 'hsv', 0, 255, empty)
# cv.createTrackbar('higher_h', 'hsv', 255, 255, empty)
# cv.createTrackbar('lower_s', 'hsv', 0, 255, empty)
# cv.createTrackbar('higher_s', 'hsv', 255, 255, empty)
# cv.createTrackbar('lower_v', 'hsv', 0, 255, empty)
# cv.createTrackbar('higher_v', 'hsv', 255, 255, empty)

# range of colors to be detected (hsv values)
colors = {
    'gold': ((45, 50, 80), (50, 100, 100)),
    'silver': ((0, 0, 75), (255, 30, 90))
}

# capturing continuous images
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

    # applying some morphological operations
    kernel = np.ones((3, 3), np.uint8)  # kernel for dilation
    img = cv.dilate(canny, kernel, iterations=2)
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

    # finding contours
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # detecting the coins
    coins = []
    for i, contour in enumerate(contours):
        # approximating the contour shape (circle)
        area = cv.contourArea(contour)
        perimeter = cv.arcLength(contour, closed=True)
        epsilon = perimeter * 0.02
        approx = cv.approxPolyDP(contour, epsilon, closed=True)

        # getting dimensions of the contour detected (x-axis, y-axis, width, height)
        x, y, w, h = cv.boundingRect(approx)

        # differentiating contour(coin) by color
        roi = image[y:y + h, x:x + w]
        if roi is not None and area > 5000:  # area set to a min threshold to increase accuracy
            # marking around the coin
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv.circle(image, (x + w // 2, y + h // 2), (w // 2), (0, 255, 0), 5)

            # getting hsv image for checking color
            hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
            for coin, (lower, upper) in colors.items():
                mask = cv.inRange(hsv_roi, np.array(lower), np.array(upper))
                if np.any(mask):
                    # add to coins list if color matched
                    coins.append((coin, area, x, y, w, h))
            # cv.imshow('contour' + str(i), hsv_roi)  # to see the detected coins in hsv

    # counting coin values
    total = 0
    for coin, area, x, y, w, h in coins:
        # differentiating based on size and displaying the value
        if area > 70000:
            total += 10
            cv.putText(image, "10", (x + w // 2, y + h // 2), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 10)
        elif 57000 < area < 59000:
            total += 2
            cv.putText(image, "2", (x + w // 2, y + h // 2), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 10)
        elif 52000 < area < 56000 and coin == 'gold':
            total += 5
            cv.putText(image, "5", (x + w // 2, y + h // 2), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 10)
        elif 50000 > area and coin == 'silver':
            total += 1
            cv.putText(image, "1", (x + w // 2, y + h // 2), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 10)

    # displaying total value
    cv.putText(image, "total = " + str(total), (50, 150), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 8)

    # # to get the hsv values of coins
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
    # print(lower_hsv, higher_hsv)
    #
    # mask = cv.inRange(hsv, lower_hsv, higher_hsv)
    # res = cv.bitwise_and(image, image, mask=mask)

    # displaying results
    cv.imshow('out', image)  # output image
    # cv.imshow('canny', img)  # canny edge
    # cv.imshow('mask',mask)  # mask applied
    # cv.imshow('res',res)  # output after applying mask

    # exit the loop by pressing 'q'
    if cv.waitKey(1) == ord('q'):
        break

# release video capture object
cap.release()
cv.destroyAllWindows()

