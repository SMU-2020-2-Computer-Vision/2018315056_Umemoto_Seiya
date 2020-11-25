import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../img/fish_60_1.5.png", 1)
print(img[0, 0, 0])
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_binary = cv2.threshold(img_gray, 127, 255, 0)
cnt, _ = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(cnt[0])
box = np.int0(cv2.boxPoints(rect))
print(box)
print(img.shape)
cv2.drawContours(img, [box], 0, (255,0,0), 2)
plt.imshow(img)
plt.show()