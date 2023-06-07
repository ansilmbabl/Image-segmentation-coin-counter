import cv2 as cv

def preProcessing(img):
    img = cv.GaussianBlur(img,(5,5),10)
    img = cv.Canny(img,50,250)
    return img