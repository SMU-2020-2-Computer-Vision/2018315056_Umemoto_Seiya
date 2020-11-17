import cv2
import os
import numpy as np

def do_nothing(x):
    pass

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

img_gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

img_edge = cv2.Canny(img_gray, 1690, 3056, apertureSize=5)

kernel = np.ones((3, 3), np.uint8)

img_dil = cv2.dilate(img_edge, kernel, iterations=1)

img_ero = cv2.erode(img_dil, kernel, iterations=1)

cv2.imshow('lena', img_ero)

winname = 'Canny Edge Detection'
cv2.namedWindow(winname)

cv2.createTrackbar('minVal', winname, 1690, 5000, do_nothing)
cv2.createTrackbar('maxVal', winname, 3056, 5000, do_nothing)
cv2.createTrackbar('iteration', winname, 3, 7, do_nothing)

while True:
    minVal = cv2.getTrackbarPos('minVal', winname)
    maxVal = cv2.getTrackbarPos('maxVal', winname)
    iteration = cv2.getTrackbarPos('iteration', winname)

    img_edge = cv2.Canny(img_gray, minVal, maxVal, apertureSize=iteration)

    cv2.imshow(winname, img_gray)
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()