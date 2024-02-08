import cv2 
import numpy as np 

img_filter = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\filter.png")
img_median = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\median.png")
img_bilateral = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\bilateral.png")

blur = cv2.blur(img_filter, (5,5)) #Blur was applied according to the values, it must be a positive odd number
blur2= cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)

median_blur = cv2.medianBlur(img_median, 11)

blur_bilateral = cv2.bilateralFilter(img_bilateral, 9,75,75)

cv2.imshow("original", img_bilateral)
cv2.imshow("bilateral", blur_bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()

