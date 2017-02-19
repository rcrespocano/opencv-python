import numpy as np
import cv2
from matplotlib import pyplot as plt

X = np.random.randint(25, 53, (25, 2))
Y = np.random.randint(57, 85, (25, 2))
Z = np.vstack((X,Y))

# Convert to np.float32
Z = np.float32(Z)

# Define criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Define number of cluters
K = 2

# Attempts
attempts = 10

# Apply kmeans
if cv2.__version__.startswith('2.4'):
    ret, label, center = cv2.kmeans(Z, K, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
else:
    ret, label, center = cv2.kmeans(Z, K, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)

# Now separate the data, Note the flatten()
A = Z[label.ravel() == 0]
B = Z[label.ravel() == 1]

# Plot the data
plt.figure(1)

plt.subplot(211)
plt.scatter(A[:,0], A[:,1], c = 'gray')
plt.scatter(B[:,0], B[:,1], c = 'gray')
plt.xlabel('Height')
plt.ylabel('Weight')

plt.subplot(212)
plt.scatter(A[:,0], A[:,1])
plt.scatter(B[:,0], B[:,1], c = 'r')
plt.scatter(center[:,0], center[:,1], s = 80, c = 'y', marker = 's')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()

