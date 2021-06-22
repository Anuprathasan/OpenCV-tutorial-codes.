import cv2
import random

img = cv2.imread('assets/nature.jpg', -1)
print (img.shape)
# Change first 100 rows to random pixels
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of image
tag = img[150:320, 250:350]
print (tag.shape)
img[10:180, 50:150] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
