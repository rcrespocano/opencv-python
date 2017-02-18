import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load
image_path = 'images/jp.jpg'
image = cv2.imread(image_path)

# Show image
cv2.imshow('Image', image)
cv2.waitKey(0)

# Histogram
color_channels = cv2.split(image)

hist_b = cv2.calcHist([color_channels[0]], channels=[0], mask=None, histSize=[256], ranges=[0,256])
hist_g = cv2.calcHist([color_channels[1]], channels=[0], mask=None, histSize=[256], ranges=[0,256])
hist_r = cv2.calcHist([color_channels[2]], channels=[0], mask=None, histSize=[256], ranges=[0,256])

# Plot
plt.plot(hist_b, c = 'blue')
plt.plot(hist_g, c = 'green')
plt.plot(hist_r, c = 'red')
plt.xlim([0, 255])
plt.show()

cv2.destroyAllWindows()
