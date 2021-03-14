import cv2
from ball_detection import detectBall
from patterntest import determinePattern

# camera = cv2.VideoCapture(0)
# width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# while True:
#     ret, frame = camera.read()
#     frame_detected, x_coords, dist = detectBall(frame, width, height)
#     pattern = determinePattern(dist, x_coords)
#     print(pattern)
#     cv2.putText(frame_detected, str(pattern), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
#     cv2.imshow('ball detection', frame_detected)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()

# TEST ON IMAGE
img = cv2.imread('ball_images/patha_red.png')
w, h = img.shape[0], img.shape[1]
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_detected, x_coords, dist = detectBall(img, w, h)
pattern = determinePattern(dist, x_coords)
cv2.putText(img_detected, str(pattern), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
cv2.imshow('ball detection', img_detected)
cv2.waitKey(0)
