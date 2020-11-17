import cv2
import os
import matplotlib.pyplot as plt

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

img_gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

img_sobelX = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
img_sobelY = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)

img_sobelX = cv2.convertScaleAbs(img_sobelX)
img_sobelY = cv2.convertScaleAbs(img_sobelY)
img_sobel = cv2.addWeighted(img_sobelX, 1, img_sobelY, 1, 0)

img_gau = cv2.GaussianBlur(img_gray, (5, 5), 0)

img_sobelX2 = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
img_sobelX2 = cv2.convertScaleAbs(img_sobelX2)

titles = ['Original', 'Gaussian', 'Derivative', 'Sobel X']
images = [img_gray, img_gau, img_sobelX2, img_sobel]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('lena', img_sobelX2)
cv2.waitKey(0)

cv2.destroyAllWindows()
