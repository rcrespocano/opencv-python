import cv2
import sys

# Load XML classifieres
cas_path = 'haarcascade/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cas_path)

# Webcam
webcam_id = 0
video_capture = cv2.VideoCapture(webcam_id)

# Detect multi-scale flags
if cv2.__version__.startswith('2.4'):
    dmf_flag = cv2.cv.CV_HAAR_SCALE_IMAGE
else:
    dmf_flag = cv2.CASCADE_SCALE_IMAGE

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Gray image
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=dmf_flag
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

