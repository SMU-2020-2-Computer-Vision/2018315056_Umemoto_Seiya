import cv2
import numpy as np
import imutils
def template_matching(img_temp, img_ref):
    h, w = img_temp.shape[:2]
    angles, scales = [x for x in range(0, 360, 10)], [0.5, 1, 1.5]
    max_value, max_pt = 0, (0, 0)
    angle, scale = 0, 0
    mask = np.full((h, w), 255, dtype=np.uint8)
    for _scale in scales:
        for _angle in angles:
            # angle_rad = _angle/180.0*np.pi
            # # イメージの中心点を基準に10度回転＋０．５間隔でスケーリング
            # M= cv2.getRotationMatrix2D((w/2, h/2), _angle, _scale)
            # # 回転後の画像サイズを計算zz
            # w_rot = int((np.round(h*np.absolute(np.sin(angle_rad))+w*np.absolute(np.cos(angle_rad))))*_scale)
            # h_rot = int((np.round(h*np.absolute(np.cos(angle_rad))+w*np.absolute(np.sin(angle_rad))))*_scale)
            # size_rot = (w_rot, h_rot)
            # # 平行移動を加える (rotation + translation)
            # affine_matrix = M.copy()
            # affine_matrix[0][2] = affine_matrix[0][2] -w/2 + w_rot/2
            # affine_matrix[1][2] = affine_matrix[1][2] -h/2 + h_rot/2

            # rot_img_temp = cv2.warpAffine(img_temp, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)
            # rot_img_temp = imutils.rotate(img_temp, _angle, center=(w/2,h/2), scale=_scale)
            res_img_temp = cv2.resize(img_temp, None, fx=_scale, fy=_scale, interpolation=cv2.INTER_CUBIC)
            res_mask = cv2.resize(mask, None, fx=_scale, fy=_scale, interpolation=cv2.INTER_CUBIC)
            rot_img_temp = imutils.rotate_bound(res_img_temp, _angle)
            rot_mask = imutils.rotate_bound(res_mask, _angle)
            data = np.zeros((rot_img_temp.shape[0], rot_img_temp.shape[1]), dtype=np.uint8)
            # _, rot_mask = cv2.threshold(rot_mask, 0.9, 1, cv2.THRESH_TOZERO)
            print(rot_img_temp.shape)
            # _, mask = cv2.threshold(rot_img_temp,200, 255,cv2.THRESH_BINARY)
            # mask = np.full((rot_img_temp.shape[0],rot_img_temp.shape[1]),255, dtype=np.uint8)
            print(data.shape)
            print(rot_mask)
            # channels = cv2.split(rot_img_temp)
            # mask = np.array(channels[0])


            #　Contourから四角形を特定。そこをROIとするのは不可能？
            # cnt, _ = cv2.findContours(rot_img_temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # rect = cv2.minAreaRect(cnt[0])
            # box = np.int0(cv2.boxPoints(rect))
            # cv2.getRectSubPix(rot_img_temp, box, size_rot)
            # cv2.drawContours(rot_img_temp, [box], -1, (255, 255, 255), 3)
            # rot_img_temp = rot_img_temp[box]

            # template matching
            _match = cv2.matchTemplate(rot_img_temp, img_ref, cv2.TM_CCORR_NORMED, data, rot_mask) #ZNCC cv2.TM_CCOEFF_NORMED
            _, _max_value, _, _max_pt = cv2.minMaxLoc(_match)
            if _max_value > max_value:
                max_value, max_pt, angle, scale = _max_value, _max_pt, _angle, _scale
    return max_pt[0], max_pt[1], angle, scale