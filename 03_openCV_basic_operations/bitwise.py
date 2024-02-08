import cv2
import numpy as np 

img1 = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\bitwise_1.png")
img2 = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\bitwise_2.png")

bit_and = cv2.bitwise_and(img2, img1) #will compare img1 and img2 at bit level

bit_or = cv2.bitwise_or(img2, img1)

bit_xor = cv2.bitwise_xor(img2, img1)

bit_not = cv2.bitwise_not(img2)

bit_not2 = cv2.bitwise_not(img1)

cv2.imshow("img_1", img1)
cv2.imshow("img_2", img2)
#cv2.imshow("bit_and", bit_and)
#cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()

#value of black dots is 0, value of white dots is 1
#making comparisons between black and white