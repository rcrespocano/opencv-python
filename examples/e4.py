import numpy as np
import cv2

video_file = 'videos/roller-coaster.mp4'
cap = cv2.VideoCapture(video_file)

# Properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255,255,255)
thickness = 1

if cv2.__version__.startswith('2.4'):
    height_prop = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT 
else:
    height_prop = cv2.CAP_PROP_FRAME_HEIGHT

if cv2.__version__.startswith('2.4'):
    fps_prop = cv2.cv.CV_CAP_PROP_FPS
else:
    fps_prop = cv2.CAP_PROP_FPS

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Text position
        height = int(cap.get(height_prop))
        position = (50, height - 50)
        
        # Frames per second
        fps = "{0:.2f}".format(cap.get(fps_prop))
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

