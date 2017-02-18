import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load
image_path = 'images/rabbit.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Show image
cv2.imshow('Image', image)
cv2.waitKey(0)

# Histogram
hist = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0,256])

# Plot
plt.plot(hist)
plt.xlim([0, 255])
plt.show()

cv2.destroyAllWindows()
