import numpy as np
import cv2
 
img = cv2.imread('images/machu_picchu.jpg')
Z = img.reshape((-1,3))
 
# Convert to np.float32
Z = np.float32(Z)

# Define criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Define number of clusters(K) 
K = 8

# Attempts
attempts = 10

# Apply kmeans
if cv2.__version__.startswith('2.4'):
    ret, label, center = cv2.kmeans(Z, K, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
else:
    ret, label, center = cv2.kmeans(Z, K, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
final_image = res.reshape((img.shape))

cv2.imshow('Original image', img)
cv2.imshow('Color Quantization', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
