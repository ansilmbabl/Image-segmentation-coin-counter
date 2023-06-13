import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture("http://192.168.1.72:8080/video")  # 0 represents the default camera

while True:
    # Read the current frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 30, 150)  # Adjust the threshold values as needed

    # Apply Hough Circle Transform
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=90, param1=50, param2=30, minRadius=100, maxRadius=200)

    # Draw the detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            # Draw outer circle
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Coin Detection', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close windows
cap.release()
cv2.destroyAllWindows()
