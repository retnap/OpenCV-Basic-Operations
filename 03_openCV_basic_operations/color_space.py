import cv2 

#Converting Color Spaces to Each Other
img = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\terim.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Terim BGR", img)
cv2.imshow("Terim RGB", img_rgb)
cv2.imshow("Terim HSV", img_hsv)
cv2.imshow("Terim Gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()