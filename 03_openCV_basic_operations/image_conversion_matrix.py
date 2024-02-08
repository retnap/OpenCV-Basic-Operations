import cv2
import numpy as np 

img = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\icardi.png", 0)

row = img.shape[0]
col = img.shape[1]

M = np.float32([[1,0,10], [0,1,70]])  #We can scroll the image on a black background.

dst = cv2.warpAffine(img, M, (row,col))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
