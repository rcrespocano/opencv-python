import cv2
import numpy as np

filename = 'images/taj-noise.jpg'
img = cv2.imread(filename)

# RGB -> Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Input image should be grayscale and float32 type
gray = np.float32(gray)

# Corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

# Show
cv2.imshow('dst', img)

# Exit?
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

