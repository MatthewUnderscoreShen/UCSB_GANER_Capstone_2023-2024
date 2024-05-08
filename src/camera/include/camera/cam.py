#!/usr/bin/env python3
from ultralytics import YOLO
from skimage import io
import os

class Camera(object):

    def __init__(self, pkg_path):
        self.pkg_path = pkg_path
        self.model = YOLO(os.path.join(self.pkg_path, "include", "camera", "best.pt"))

    def detect_object(self):
        os.system('raspistill -o /home/capstone/UCSB_GANER_Capstone_2023-2024/src/camera/include/camera/image.jpg -h 640 -w 640 -t 10 -rot 0')
        path = os.path.join(self.pkg_path, "include", "camera", "image.jpg")
        results = self.model([path])  # return a list of Results objects
        xyxy = results[0].boxes.xyxy.numpy()
        return xyxy