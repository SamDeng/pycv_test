import cv2
import numpy as np

def MultiMaxLocation(src, score):
    threshold = score*0.5
    result = np.empty(np.shape
    result_image = np.empty(src.shape,src.dtype)
    result_image = src
    count = 0
    for(i, j), srcdata in np.ndenumerate(src):
        if(srcdata>threshold):
            roi = src[i:i+50, j:j+50]
            maxvalue = np.max(roi)
            location = np.unravel_index(np.argmax(roi), roi.shape)
            #location = location[: + (i, j)
            if(maxvalue>score):
                result[count, 0] = i + location[0]
                result[count, 1] = j + location[1]
                count = count+1
                cv2.rectangle(result_image, (10, 10), (20, 20), 255, 3)
            src[i:i+20, j:j+20] = 0
    return (result, result_image)



