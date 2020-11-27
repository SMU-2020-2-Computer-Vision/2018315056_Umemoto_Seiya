import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from hw02_2018315056_template_matching import template_matching

if __name__ == "__main__":
    # Set the working directory to be the current one
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Load a reference image as grayscale
    img_reference = cv2.imread('../img/sample1.png', 0)

    # Load a template image as grayscale
    img_template = cv2.imread('../img/fish.png', 0)

    # Apply template matching
    x, y, angle, scale = template_matching(img_template, img_reference)

    h, w = img_template.shape[:2]

    # 회전 후의 사이즈 구하기
    angle_rad = angle/180.0*np.pi
    w_rot = int((np.round(h*np.absolute(np.sin(angle_rad))+w*np.absolute(np.cos(angle_rad))))*scale)
    h_rot = int((np.round(h*np.absolute(np.cos(angle_rad))+w*np.absolute(np.sin(angle_rad))))*scale)

    # 사각 영역 그리기
    cv2.rectangle(img_reference, (x, y), (x+w_rot, y+h_rot), 0, 2)

    plt.imshow(img_reference,cmap='gray')
    plt.title("Detected Point"), plt.xticks([]), plt.yticks([])
    plt.show()