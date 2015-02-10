import cv2
import numpy as np

def shift_dft(src, dst):
    
    if dst is None:
        dst = np.empty(src.shape, src.dtype)
    elif src.shape != dst.shape:
        raise ValueError("src and dst must have equal sizes")
    elif src.dtype != dst.dtype:
        raise TypeError("src and dst must have equal type")

    if src is dst:
        ret = np.empty(src.shape, src.dtype)
    else:
        ret = dst

    h, w = src.shape[:2]

    cx1 = cx2 = w/2
    cy1 = cy2 = h/2

    if w%2 != 0:
        cx2 += 1
    if h%2 != 0:
        cy2 += 1

    #swap quadrants
    ret[h-cy1:, w-cx1:] = src[0:cy1, 0:cx1 ]
    ret[0:cy2, 0:w-cx2] = src[h-cy2:, h-cx2:]

    ret[h-cy1:, 0:cx1] = src[0:cy1, w-cx1:]
    ret[0:cy1, w-cx2:] = src[h-cy2:, 0:cx2]

    if src is dst:
        dst[:, :] = ret

    return dst

im = cv2.imread("test_image/alpha1.png", cv2.IMREAD_UNCHANGED)
h, w = im.shape[:2]

realinput = im.astype(np.float64)

dft_m = cv2.getOptimalDFTSize(w)
dft_n = cv2.getOptimalDFTSize(h)

dft_a = np.zeros((dft_n, dft_m, 2), dtype = np.float64)
dft_a[:h, :w, 0] = realinput

cv2.dft(dft_a, dst=dft_a, nonzeroRows=h)

cv2.imshow("win", im)

image_re, image_im = cv2.split(dft_a)

magnitude = cv2.sqrt(image_re**2 + image_im**2)

log_spectrum = cv2.log(1.0 + magnitude)

shift_dft(log_spectrum, log_spectrum)

cv2.normalize(log_spectrum, log_spectrum, 0.0, 1.0, cv2.NORM_MINMAX)

cv2.imshow("mag", log_spectrum)


cv2.waitKey(100000)
