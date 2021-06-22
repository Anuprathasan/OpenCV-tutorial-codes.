import cv2

img = cv2.imread('assets/rainbow.png', 1)
cv2.imshow('Image 1', img)

img = cv2.resize(img, (0,0), fx=2, fy=2)
img = cv2.rotate(img, cv2.cv2.ROTATE_180)

cv2.imwrite('assets/new_img_.png', img)

cv2.imshow('Image 2', img)
cv2.waitKey(0 )
cv2.destroyAllWindows(0)
 
 
