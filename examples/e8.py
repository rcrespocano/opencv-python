import cv2

# Load image
image_path = 'images/sunset.jpg'
image = cv2.imread(image_path)

# Gaussian blur
k = 5
sigma = 50
blur = cv2.GaussianBlur(image, (k, k), sigma)

# Show
cv2.imshow('Original', image)
cv2.imshow('Filtered', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

