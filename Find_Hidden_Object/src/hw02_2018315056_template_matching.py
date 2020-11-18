import cv2
def template_matching(img_temp, img_ref):
    WIDTH, HEIGHT = img_temp.shape[::-1]
    angles, scales = [x for x in range(0, 360, 10)], [0.5, 1, 1.5]
    max_value, max_pt = 0, (0, 0)
    angle, scale = 0, 0
    for _angle in angles:
        for _scale in scales:
            # 이미지의 중심점을 기준으로 10도 회전 하면서 0.5배 Scale
            M= cv2.getRotationMatrix2D((WIDTH/2, HEIGHT/2), _angle, _scale)
            rot_img_temp = cv2.warpAffine(img_temp, M,(WIDTH, HEIGHT))
            # template matching
            match = cv2.matchTemplate(rot_img_temp, img_ref, cv2.TM_CCOEFF_NORMED) #ZNCC
            _, _max_value, _, _max_pt = cv2.minMaxLoc(match)
            if _max_value > max_value:
                max_value, max_pt, angle, scale = _max_value, _max_pt, _angle, _scale
    return max_pt[0], max_pt[1], angle, scale