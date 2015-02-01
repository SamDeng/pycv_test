import cv2
import sqlite3


image = cv2.imread("test_image\\alpha1.png")
pr = cv2.pyrDown(image, None)

while 1:
    cv2.imshow("prydown", pr)
    cv2.imshow("origin", image)
    cv2.waitKey(20)


print "hi"