import cv2

# Load image
image_path = 'images/salt_pepper_noise.png'
image = cv2.imread(image_path)

# Gaussian blur
k = 5
blur = cv2.medianBlur(image, k)

# Show
cv2.imshow('Original', image)
cv2.imshow('Filtered', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

