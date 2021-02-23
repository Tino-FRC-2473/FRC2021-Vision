import cv2
import numpy as np
import imutils

RADIUS_THRESH = 25 #modify
KNOWN_RADIUS = 3.5 #in

def detectBall(frame):
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([22, 28, 82])  # values from field image #fix this range
    higher_yellow = np.array([30, 255, 255])  # values from field image

    mask = cv2.inRange(hsv_frame, lower_yellow, higher_yellow)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        max_cnt = max(cnts, key = cv2.contourArea)
        for cnt in cnts:
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)

            # FOR DETERMINING DISTANCE TO CLOSEST BALL:
            # if any(cnt[0][0] == max_cnt[0][0]):
            #     dist = distance(focal_length, known_radius, radius)
            #     cv2.putText(frame, '{} in'.format(str(dist)), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

            if radius >= RADIUS_THRESH:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)

    return mask, frame


def distance(flength, kwidth, pwidth):
    return round(((kwidth * flength) / pwidth) / 12, 1)


def focal(klength, kwidth, pwidth):
    return (pwidth * klength) / kwidth
