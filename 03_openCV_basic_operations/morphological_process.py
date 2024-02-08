#Erosion of Pictures

import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\icardi.png", 0)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
#As the iteration increases, the image becomes black and distorted.

dilation = cv2.dilate(img, kernel, iterations = 5)
#It gets thicker as the iteration increases.

cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()