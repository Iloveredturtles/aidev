import cv2  # dijelaskan di bagian a
# Add the code below
import numpy as np

img = cv2.imread("avenger.jpg") # explained in section b
# img = cv2.resize(img, (0,0), fx=0, fy=0.5)
# img = cv2.blur(img, (10,10))
# img = cv2.boxFilter(img, -1, (10, 10))
# img = cv2.GaussianBlur(img, (3,3), 7)
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (160,200), 165, 255, -1) 
img = cv2.bitwise_and(img, img, mask = mask) 
cv2.imshow("Mask", mask)

cv2.imshow("Image", img)  # explained in section c

cv2.waitKey(0)
cv2.destroyAllWindows() # explained in section d``

print(img.shape)

