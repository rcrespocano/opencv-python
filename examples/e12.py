import cv2
import numpy as np

webcam_id = 0
cap = cv2.VideoCapture(webcam_id)

# Cany edge detector thresholds
threshold_one = 50
threshold_two = 150
aperture_size = 3

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Operations on the frame
        edges = cv2.Canny(frame, threshold_one, threshold_two, aperture_size)
        
        # Display
        cv2.imshow("Original", frame)
        cv2.imshow("Canny edge detection", edges)

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

