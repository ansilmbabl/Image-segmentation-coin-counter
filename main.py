# importing needed modules
import cv2 as cv

cap = cv.VideoCapture(0)  # creating video capture object
cap.set(3, 640)  # setting width of frame
cap.set(4, 480)  # setting height of frame

# capturing video (images) for detecting object using a while loop
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        cv.imshow("window", img)
    if cv.waitKey(1) == ord('q'):  # stop capturing when user interrupts
        break

cap.release()  # deallocates memory and clears
cv.destroyAllWindows()
