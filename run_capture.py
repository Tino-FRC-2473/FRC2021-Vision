#!/usr/bin/env python3
import time
import argparse
import cv2
import os
from capture_image import CaptureImage
from video_live_generator import VideoLiveGenerator
from power_port_detector import PowerPortDetector

parser = argparse.ArgumentParser()
parser.add_argument("dir_name", help="directory to save images to")
parser.add_argument("port", help="camera port to read from")
args = parser.parse_args()

generator = VideoLiveGenerator(args.port)
wait_time = 3
target_detector = PowerPortDetector(generator)

if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)

with CaptureImage(target_detector) as c:

    angle = input("angle: ")
    distance = input("distance: ")

    while True:
        c.update_frame()
        key = cv2.waitKey(wait_time)
        # pos = (generator.get_frame().shape[1] /2, generator.get_frame().shape[0]/2)
        pos = (100, 50)

        cv2.drawMarker(generator.get_frame(),pos, (255, 0, 0), cv2.MARKER_CROSS, 20, 10, cv2.LINE_8)

        if key == ord('q'):
            break
        if key == ord('c'):
            c.capture(args.dir_name, angle, distance)
            if input("continue? (y/n) ") == "n":
                break

            angle = input("angle: ")
            distance = input("distance: ")