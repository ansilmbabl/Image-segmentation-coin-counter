import cv2

# Mobile device IP camera URL
url = 'http://192.168.1.71:6677/video'  # Replace 'your_ip_address' with the IP address from the IP Webcam app

# Create a VideoCapture object
cap = cv2.VideoCapture('https://www.youtube.com/watch?v=-iN7NDbDz3Q&t=2459s')

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to connect to the camera!")
    exit()

# Read and display frames from the camera
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame!")
        break

    cv2.imshow('Mobile Camera', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()
