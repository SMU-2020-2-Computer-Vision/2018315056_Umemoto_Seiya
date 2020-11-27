import cv2
import numpy as np
import imutils
def template_matching(img_temp, img_ref):
    # 변수 초기화
    max_value, max_pt = 0, (0, 0)
    angle, scale = 0, 0
    # mask = np.full((h, w), 255, dtype=np.uint8) # 흰색 사각형 마스크
    for _scale in np.linspace(0.5, 1.5, 3):
        for _angle in range(0, 360, 10):
            # 물고기를 확대/축소
            res_img_temp = cv2.resize(img_temp, None, fx=_scale, fy=_scale, interpolation=cv2.INTER_CUBIC)
            # res_mask = cv2.resize(mask, None, fx=_scale, fy=_scale, interpolation=cv2.INTER_CUBIC) # 마스크를 확대/축소

            # 물고기를 회전
            rot_img_temp = imutils.rotate_bound(res_img_temp, _angle)
            # rot_mask = imutils.rotate_bound(res_mask, _angle) # 마스크를 회전

            #template matching
            _match = cv2.matchTemplate(image=img_ref, templ=rot_img_temp, method=cv2.TM_CCOEFF_NORMED, mask=None) #마스크쓰는 경우 mask=rot_mask
            _, _max_value, _, _max_pt = cv2.minMaxLoc(_match)
            if _max_value > max_value:
                max_value, max_pt, angle, scale = _max_value, _max_pt, _angle, _scale
    return max_pt[0], max_pt[1], angle, scale