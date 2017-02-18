import cv2
import numpy as np

# Load image
image = cv2.imread('images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel
k = 3
sobelx = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=k)
sobely = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=k)

# Show
cv2.imshow('Original', image)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

