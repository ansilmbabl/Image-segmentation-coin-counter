import cv2 as cv

def window(window_name, image = "", width = 1000, height = 534):
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.resizeWindow(window_name, width, height)
    if image != "":
        cv.imshow(window_name,image)