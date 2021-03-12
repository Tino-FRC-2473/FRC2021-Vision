import cv2
import numpy as np

KNOWN_DIAMETER_PX = 156 #px
KNOWN_DISTANCE = 90 #in
KNOWN_DIAMETER_IN = 7 #in
FOCAL_LENGTH = 2005.714286

RADIUS_THRESH = 25  # modify
KNOWN_RADIUS = 3.5  # in


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
    cnts = grab_contours(cnts)

    if len(cnts) > 0:
        max_cnt = max(cnts, key=cv2.contourArea)
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


def grab_contours(cnts):
    # if the length the contours tuple returned by cv2.findContours
    # is '2' then we are using either OpenCV v2.4, v4-beta, or
    # v4-official
    if len(cnts) == 2:
        cnts = cnts[0]

    # if the length of the contours tuple is '3' then we are using
    # either OpenCV v3, v4-pre, or v4-alpha
    elif len(cnts) == 3:
        cnts = cnts[1]

    # otherwise OpenCV has changed their cv2.findContours return
    # signature yet again and I have no idea WTH is going on
    else:
        raise Exception(("Contours tuple must have length 2 or 3, "
            "otherwise OpenCV changed their cv2.findContours return "
            "signature yet again. Refer to OpenCV's documentation "
            "in that case"))

    # return the actual contours array
    return cnts
