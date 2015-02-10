import cv2
import numpy as np
import matchtemplate_test


#def matchTemplate(template,
#                  src,
#                  angle,
#                  score,
#                  result):
#    templatesize = template.size()
#    srcsize = src.size();

#def getPyrDownImage(src,
#                    level):

#def matchWithAngle(template,
#                   src,
#                   angle,
#                   step,
#                   shift):

#def rotateImage(src, angle):


roi_row1 = 275 #DE roi rectangle
roi_col1 = 109
roi_row2 = 317
roi_col2 = 160

image = cv2.imread("test_image\\alpha1.png", cv2.IMREAD_UNCHANGED)
template = image[roi_row1:roi_row2, roi_col1:roi_col2];
match = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
match_show = cv2.convertScaleAbs(match, None, 255)
[minvalue, maxvalue, minlocation, maxlocation] = cv2.minMaxLoc(match)
#[minvalue, maxvalue, minlocation, maxlocation] = cv2.minMaxLoc(match_show)
location = matchtemplate_test.MultiMaxLocation(match, 0.9)


pr = cv2.pyrDown(image)
threvalue, thre = cv2.threshold(match, 0.5, 1, cv2.THRESH_BINARY)
erod = cv2.erode(thre, np.ones([5, 5]))
match_show = 255*thre

while 1:
    #cv2.imshow("prydown", pr)
    #cv2.imshow("origin", image)
    #cv2.imshow("template", template)
    cv2.imshow("match_show", match_show)
    cv2.imshow("erod", erod)
    cv2.waitKey(20)
    

print "hi"