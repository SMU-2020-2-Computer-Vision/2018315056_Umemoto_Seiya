import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_reference = cv2.imread('../img/test_background.png', 0)
h, w = img_reference.shape[:2]
print(f'image height and width = {h}x{w}')

# Load a template image as grayscale
img_template = cv2.imread('../img/fish.png', 0)
h, w = img_template.shape[:2]
print(f'image height and width = {h}x{w}')

_angle = 150
_scale = 1.5
angle_rad = _angle/180.0*np.pi

# 回転後の画像サイズを計算
w_rot = int((np.round(h*np.absolute(np.sin(angle_rad))+w*np.absolute(np.cos(angle_rad))))*_scale)
h_rot = int((np.round(h*np.absolute(np.cos(angle_rad))+w*np.absolute(np.sin(angle_rad))))*_scale)
size_rot = (w_rot, h_rot)

# 이미지의 중심점을 기준으로 10도 회전 하면서 0.5배 Scale
M= cv2.getRotationMatrix2D((w/2, h/2), _angle, _scale)

# 平行移動を加える (rotation + translation)
affine_matrix = M.copy()
affine_matrix[0][2] = affine_matrix[0][2] -w/2 + w_rot/2
affine_matrix[1][2] = affine_matrix[1][2] -h/2 + h_rot/2

rot_img_template = cv2.warpAffine(img_template, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)
h, w = rot_img_template.shape[:2]
cv2.imshow("a", rot_img_template)
cv2.waitKey(0)

img_reference[250:250+h, 150:150+w] = rot_img_template

cv2.imwrite(r"../img/test_ref1.png", img_reference)
