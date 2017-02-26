import cv2
import numpy as np

# Webcam
webcam_id = 0
cap = cv2.VideoCapture(webcam_id)

while True:
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range in HSV
    lower_color = np.array([0, 70, 50])
    upper_color =  np.array([10, 255, 255])

    # Mask: threshold the HSV image to get only defined colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Show
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Color', res)

    # Exit?
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

