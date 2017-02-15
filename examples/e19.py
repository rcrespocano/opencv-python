import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
path = 'images/bratislava_castle.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Initiate ORB detector
orb = cv2.ORB()

# Find the keypoints and descriptors with ORB
kp, des = orb.detectAndCompute(img, None)

# Draw only keypoints location, not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
cv2.imshow('Keypoints', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

