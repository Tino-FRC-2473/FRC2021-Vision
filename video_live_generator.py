import cv2
import numpy as np
import subprocess


class VideoLiveGenerator:
    def __init__(self, input_port):
        self.input_port = str(input_port)
        self.input = cv2.VideoCapture(str(input_port))
        self.set_camera_settings(str(input_port))

        self.input.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.input.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        frame = self.get_frame()
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH = frame.shape[:2]

        self.H_FIELD_OF_VIEW = 68.37
        self.V_FIELD_OF_VIEW = 41.21

    def __enter__(self):
        return self

    def set_camera_settings(self, camera_port):
        camera_path = camera_port

        try:
            subprocess.call(["v4l2-ctl", "-d", camera_path, "-c", "exposure_auto=1"])
            subprocess.call(["v4l2-ctl", "-d", camera_path, "-c", "exposure_absolute=100"])
            subprocess.call(["v4l2-ctl", "-d", camera_path, "-c", "white_balance_temperature_auto=1"])
        except FileNotFoundError:
            print("exposure adjustment not completed")

    def get_frame(self):
        _, frame = self.input.read()
        # frame = np.rot90(frame, 3).copy()
        return frame

    def get_horizontal_fov(self):
        return self.H_FIELD_OF_VIEW

    def get_vertical_fov(self):
        return self.V_FIELD_OF_VIEW

    def generate(self):
        frame = self.get_frame()
        return frame, None
