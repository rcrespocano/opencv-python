import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
path = 'images/bratislava_castle.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# ORB
orb = cv2.ORB()
kp_orb, des = orb.detectAndCompute(img, None)
img_orb = cv2.drawKeypoints(img, kp_orb, None, color=(0, 255, 0), flags=0)

# SIFT
sift = cv2.xfeatures2d.SIFT_create()
kp_sift = sift.detect(gray, None)
img_sift = cv2.drawKeypoints(img, kp_sift, None, color=(255, 0, 0), flags=0)

# FAST
fast = cv2.FastFeatureDetector_create()
kp_fast = fast.detect(img, None)
img_fast = cv2.drawKeypoints(img, kp_fast, None, color=(0, 0, 255), flags=0)

# Draw
cv2.imshow('ORB', img_orb)
cv2.imshow('SIFT', img_sift)
cv2.imshow('SIFT', img_fast)
cv2.waitKey(0)
cv2.destroyAllWindows()

