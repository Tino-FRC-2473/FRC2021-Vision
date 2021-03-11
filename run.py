import cv2
from ball_detection import detectBall
from patterntest import determinePattern

img = cv2.imread('ball_images/patha_red.png')
w, h = img.shape[0], img.shape[1]
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_detected, x_coords,dist, mask = detectBall(img, w, h)
pattern = determinePattern(dist, x_coords[0], x_coords[1], x_coords[2])
cv2.putText(img_detected, str(pattern), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

cv2.imshow('ball detection', img_detected)
cv2.waitKey(0)
cv2.destroyAllWindows()


