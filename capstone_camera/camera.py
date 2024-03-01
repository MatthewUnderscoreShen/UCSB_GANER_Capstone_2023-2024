from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import os
os.system('raspistill -o image1.jpg -w 640 -h 480 -t 10 -vf')
img = io.imread('image1.jpg')
plt.figure()
plt.imshow(img)
plt.show()
