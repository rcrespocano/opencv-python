import numpy as np
import cv2

webcam_id = 0
cap = cv2.VideoCapture(webcam_id)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Operations on the frame
        v_frame = cv2.flip(frame, 1)
        h_frame = cv2.flip(frame, 0)
        
        # Display
        cv2.imshow("Original", frame)
        cv2.imshow("Vertical flip", v_frame)
        cv2.imshow("Horizontal flip", h_frame)

        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

