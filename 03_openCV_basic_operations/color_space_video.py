#Converting Video's Color Space

import cv2 

cap = cv2.VideoCapture("C:\\Users\\Selman\\opencv_udemy\\01_core_operations\\test_images\\edit.mp4")

while True:
    ret, frame = cap.read() 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()