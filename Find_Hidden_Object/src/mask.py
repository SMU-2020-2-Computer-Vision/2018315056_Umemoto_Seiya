import cv2
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../img/fish.png", 0)
_, img_thre = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
print(img_thre)

cv2.imshow("",img_thre)
cv2.waitKey(0)