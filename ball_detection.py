import cv2
import numpy as np

# known diamter of ball from 90in way (not accounting for angle)
KNOWN_DIAMETER_PX = 156  # px
# known distance from cam to closest ball (7.5', not accounting for angle)
KNOWN_DISTANCE = 90  # in
# known diameter of ball
KNOWN_DIAMETER_IN = 7  # in
# focal len = 90 * 156 / 7
FOCAL_LENGTH = 2005.714286  # px

RADIUS_THRESH = 25  # modify
KNOWN_RADIUS = 3.5  # in
RADIUS_THRESH = 10  # modify

CROP_HEIGHT = 145  # crop the height of the frame to hide other yellow objects


def distance(flength, kwidth, pwidth):
    dist = ((kwidth * flength) / pwidth) / 12
    print("DISTANCE: ", dist)
    return round(dist, 1)

def detectBall(frame):
    w, h = frame.shape[1], frame.shape[0]
    x_coords = []
    dist = 0
    output = frame.copy()
    lower_yellow = np.array([17, 130, 130])  # values from field image; fix this range
    higher_yellow = np.array([30, 255, 255])  # values from field image

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_frame = cv2.GaussianBlur(hsv_frame, (5, 5), 0)
    mask = cv2.inRange(hsv_frame, lower_yellow, higher_yellow)
    mask = cv2.erode(mask, None, iterations=7)
    mask = cv2.dilate(mask, None, iterations=10)

    mask = mask[CROP_HEIGHT:h, 0:w]  # crop the image to hide other yellow objects
    output = output[CROP_HEIGHT:h, 0:w]

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]  # simplified grab contours method

    if len(cnts) > 0:
        max_cnt = max(cnts, key=cv2.contourArea)  # closest ball
        _, radius = cv2.minEnclosingCircle(max_cnt)
        dist = distance(FOCAL_LENGTH, KNOWN_DIAMETER_IN, radius * 2)
        print("DIST: ", dist)
        for cnt in cnts:
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            print("RADIUS: ", radius)
            if radius >= RADIUS_THRESH:
                x_coords.append(x)
                cv2.circle(output, (int(x), int(y)), int(radius), (0, 255, 0), 2)

    return output, x_coords, dist

