from ultralytics import YOLO
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import os

import os
# Load a model
model = YOLO('best.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of image
while 1:
	print("enter something to continue")
	input()
	os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
	results = model(['image.jpg'])  # return a list of Results objects
	xyxy = results[0].boxes.xyxy.numpy()
	print(xyxy)
	# show the result, comment out this
	img = io.imread('image.jpg')
	plt.figure()
	plt.imshow(img)
	if xyxy.size == 0:
		print("warning, the box is not detected")
	else:
		plt.plot(xyxy[0][0],xyxy[0][1],"or",markersize = 5)
		plt.plot(xyxy[0][2],xyxy[0][3],"or",markersize = 5)
		plt.plot((xyxy[0][0]+xyxy[0][2])/2,(xyxy[0][1]+xyxy[0][3])/2,"bD",markersize = 5)
	plt.show()
