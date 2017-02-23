import cv2

# Load
image_path = 'images/rabbit.jpg'
image = cv2.imread(image_path)

# Save copy as png
image_copy_path = 'images/rabbit-copy.png'
cv2.imwrite(image_copy_path, image)

# Load copy
image_copy = cv2.imread(image_copy_path)

# Show
cv2.imshow('Original', image)
cv2.imshow('Copy', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

