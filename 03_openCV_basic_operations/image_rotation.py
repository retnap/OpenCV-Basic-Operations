import cv2
import numpy as np 

img = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\icardi.png", 0)

row = img.shape[0]
col = img.shape[1]

M = cv2.getRotationMatrix2D((col/2, row/2), 90, 1)
#rotate 90 degrees counterclockwise

dst = cv2.warpAffine(img, M, (col,row))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()