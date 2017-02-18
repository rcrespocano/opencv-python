import cv2
import numpy as np

filename = 'images/church.png'
img = cv2.imread(filename)

# RGB -> Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Input image should be grayscale and float32 type
gray = np.float32(gray)

# Corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Show
cv2.imshow('dst',img)

# Exit?
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

