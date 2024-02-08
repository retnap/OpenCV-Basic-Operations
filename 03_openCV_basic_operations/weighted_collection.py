# Weighted addition is adding images on top of each other at specific densities.
# f(x,y) = x*a + y*b + c 

import cv2
import numpy as np 

circle = np.zeros((512,512,3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255,0,0), -1)

rectangle = np.zeros((512,512,3), np.uint8) + 255
cv2.rectangle(rectangle, (150,150), (350,350), (0,0,255), -1)

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)
#circle by 0.7 rectangle by 0.3 added totals 1 fixed number 0


cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("AddWeighted", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()