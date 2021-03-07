import cv2
import numpy as np
import imutils

KNOWN_DIAMETER_PX = 156 #px
KNOWN_DISTANCE = 90 #in
KNOWN_DIAMETER_IN = 7 #in
FOCAL_LENGTH = 2005.714286

RADIUS_THRESH = 10 #modify


def distance(flength, kwidth, pwidth):
    dist = ((kwidth * flength) / pwidth) / 12
    print("DISTANCE: ", dist)
    return round(dist, 1)

def detectBall(frame, w, h):
    x_coords = []
    output = frame.copy()
    lower_yellow = np.array([17, 130, 130])  # values from field image #fix this range
    higher_yellow = np.array([30, 255, 255])  # values from field image

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_frame = cv2.GaussianBlur(hsv_frame, (5, 5), 0)
    mask = cv2.inRange(hsv_frame, lower_yellow, higher_yellow)
    mask = cv2.erode(mask, None, iterations=7)
    mask = cv2.dilate(mask, None, iterations=10)

    mask = mask[145:h, 0:w]
    output = output[145:h, 0:w]

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        max_cnt = max(cnts, key = cv2.contourArea)
        for cnt in cnts:
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            print(radius)

            # FOR DETERMINING DISTANCE TO CLOSEST BALL:
            if any(cnt[0][0] == max_cnt[0][0]):
            # dist = 10 #ft
                dist = distance(FOCAL_LENGTH, KNOWN_DIAMETER_IN, radius*2)
                #cv2.putText(frame, '{} in'.format(str(dist)), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

            if radius >= RADIUS_THRESH:
                x_coords.append(x)
                cv2.circle(output, (int(x), int(y)), int(radius), (0, 255, 0), 2)

    return output, x_coords, dist, mask
    # return mask, dist if needed


