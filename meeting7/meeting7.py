import cv2  # dijelaskan di bagian a

img = cv2.imread("exercise.jpg") # explained in section b
# img = cv2.resize(img, (0,0), fx=0, fy=0.5)
# img = cv2.blur(img, (10,10))
# img = cv2.boxFilter(img, -1, (10, 10))
img = cv2.GaussianBlur(img, (3,3), 7)
cv2.imshow("Image", img)  # explained in section c

cv2.waitKey(0)
cv2.destroyAllWindows() # explained in section d``

print(img.shape)

