import cv2
import numpy as np

# All the 6 methods for comparison in a list
method = eval('cv2.TM_CCORR_NORMED')

angles = [x for x in range(0, 360, 10)]

scales = [0.5, 1, 1.5]

fin_max_value = 0
fin_pt = 0
fin_angle = 0
fin_scale = 0

def template_matching(img_temp, img_ref):
    global fin_max_value
    w, h = img_temp.shape[::-1]
    for angle in angles:
        for scale in scales:
            # 이미지의 중심점을 기준으로 10도 회전 하면서 0.5배 Scale
            M= cv2.getRotationMatrix2D((w/2, h/2), angle, scale)
            rot_img_temp = cv2.warpAffine(img_temp, M,(w, h))

            # gray_rot_img = cv2.cvtColor(rot_img, cv2.COLOR_RGB2GRAY)

            # template matching
            match = cv2.matchTemplate(rot_img_temp, img_ref, cv2.TM_CCOEFF_NORMED)#ZNCC
            min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
            if fin_max_value > 0 and max_value > fin_max_value:
                fin_max_value = max_value
                fin_pt = max_pt
                fin_angle = angle
                fin_scale = scale                
            elif fin_max_value == 0:
                fin_max_value = max_value
    return fin_pt[0], fin_pt[1], fin_angle, fin_scale