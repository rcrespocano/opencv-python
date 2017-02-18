import cv2
import numpy as np

# Load image
image = cv2.imread('images/taj-noise.jpg', cv2.IMREAD_GRAYSCALE)

# Gaussian
k = 5
sigma = 20
image_gaussian = cv2.GaussianBlur(image, (k, k), sigma)

# Laplacian
laplacian_without_filter = cv2.Laplacian(image, cv2.CV_64F)
laplacian_with_filter = cv2.Laplacian(image_gaussian, cv2.CV_64F)

# Show
cv2.imshow('Original', image)
cv2.imshow('Gaussian', image_gaussian)
cv2.imshow('Laplacian without Gaussian', laplacian_without_filter)
cv2.imshow('Laplacian with Gaussian', laplacian_with_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
