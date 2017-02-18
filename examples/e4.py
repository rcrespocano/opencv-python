import numpy as np
import cv2

video_file = 'videos/roller-coaster.mp4'
cap = cv2.VideoCapture(video_file)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255,255,255)
thickness = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Text position
        height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        position = (50, height - 50)
        
        # Frames per second
        fps = "{0:.2f}".format(cap.get(cv2.cv.CV_CAP_PROP_FPS))
        text = "FPS: " + fps
        
        # Put text
        cv2.putText(frame, text, position, font, font_scale, color, thickness)

        # Display
        cv2.imshow("Video", frame)
        
        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

