import argparse
import cv2
from ball_detection import detectBall
from patterntest import determinePattern
from data_sender import DataSender

parser = argparse.ArgumentParser()
parser.add_argument("type", help="use camera feed or image")  # camera or image
# NEW COMMAND LINE ARGUMENT FOR POTENTIAL TEST IMAGE PROBLEMS
parser.add_argument("test", help="test the program or take test pictures")  # prog for test program, pic for taking pictures
parser.add_argument("-p", "--port", type=int, help="camera port to read from")
parser.add_argument("-i", "--image", help="path to input image")
args = parser.parse_args()

sender = DataSender()

if args.type == "camera":
    camera = cv2.VideoCapture(args.port)
    while True:
        ret, frame = camera.read()

        if args.test == "prog":  # if statement surrounding all ball detection/pattern frames
            frame_detected, x_coords, dist = detectBall(frame)
            pattern = determinePattern(dist, x_coords)
            sender.send_data(pattern)
            cv2.putText(frame_detected, str(pattern), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.imshow('ball detection', frame_detected)
        else:
            cv2.imshow('raw frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

elif args.type == 'image':
    img = cv2.imread(args.image)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    if args.test == "prog":  # if statement surrounding all ball detection/pattern frames
        img_detected, x_coords, dist = detectBall(img)
        pattern = determinePattern(dist, x_coords)
        sender.send_data(pattern)
        cv2.putText(img_detected, str(pattern), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        cv2.imshow('ball detection', img_detected)
    else:
        cv2.imshow('raw frame', img)

    cv2.waitKey(0)
