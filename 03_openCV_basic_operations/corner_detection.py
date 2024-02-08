import cv2
import numpy as np 

img = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\text.png")
img1 = cv2.imread("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
# in gray, maximum number of edges, quality value, minimum distance between corners
# If you increase the value to 50, it tries to find more corners

corners = np.int0(corners)   #Converted corners to int again

for corner in corners:
    x,y = corner.ravel()  #apply ravel to corner, write in a single line format
    cv2.circle(img, (x,y), 3, (0,0,255), -1)

cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
