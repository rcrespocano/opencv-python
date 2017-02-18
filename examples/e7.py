import cv2

# Load image
image_path = 'images/sunset.jpg'
image = cv2.imread(image_path)

# Blur
k = 5
blur = cv2.blur(image, (k, k))

# Show
cv2.imshow('Original', image)
cv2.imshow('Filtered', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

