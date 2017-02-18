import cv2
from matplotlib import pyplot as plt

# Load
image_path = 'images/rabbit.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Histogram & plot
plt.hist(image.ravel(), 256, [0, 256]);
plt.xlim([0, 255])
plt.show()

