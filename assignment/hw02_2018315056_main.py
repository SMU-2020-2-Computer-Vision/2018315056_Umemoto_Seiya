import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from hw02_2018315056_template_matching import template_matching

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_reference = cv2.imread('rot_messi.jpg', 0)

# Load a template image as grayscale
img_template = cv2.imread('messi_face.jpg', 0)
w, h = img_template.shape[::-1]

# Apply template matching
x, y, angle, scale = template_matching(img_template, img_reference)

print(x, y, angle, scale)

bottom_right = (x + w, y + h)

# # Draw a bounding box
cv2.rectangle(img_reference, (x, y), bottom_right, 255, 2)

plt.subplot(121),plt.imshow(img_reference,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_reference,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle("TM_CCOEFF_NORMED")

plt.show()