import cv2
import numpy as np

image_file = 'images/rabbit.jpg'
img = cv2.imread(image_file)

kernel = np.ones((3, 3), np.float32) / 9
dst = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

# Show
cv2.imshow('Original', img)
cv2.imshow('Filtered', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

