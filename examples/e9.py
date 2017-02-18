import cv2

# Load image
image_path = 'images/lena_noise.jpg'
image = cv2.imread(image_path)

# Gaussian blur
k = 5
sigma = 0
blur = cv2.GaussianBlur(image, (k, k), sigma)

# Show
cv2.imshow('Original Lena with noise', image)
cv2.imshow('Filtered Lena', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

