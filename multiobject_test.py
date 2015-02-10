import cv2
import numpy as np
import matchtemplate_test


image = cv2.imread("test_image\\template\\sample_image.tif", cv2.IMREAD_UNCHANGED)
template = cv2.imread("test_image\\template\\sample_template.tif", cv2.IMREAD_UNCHANGED)

match = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
threvalue, thre = cv2.threshold(match, 0.5, 1, cv2.THRESH_BINARY)
(location, result_image) = matchtemplate_test.MultiMaxLocation(match, 0.7)
match_show = 255*thre

match_origin = 255*match

while 1:
    cv2.imshow("match_show",  match_show)
    cv2.imshow("result", result_image)
    cv2.imshow("result_origin", match_origin)
    cv2.imshow("origin", image)
    cv2.waitKey(20)

