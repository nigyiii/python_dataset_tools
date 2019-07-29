import cv2
import numpy as np
import random

img = np.ones((30, 30), dtype=np.uint8)
bgr_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

bgr_img[:,:,0] = random.randint(0, 255)
bgr_img[:,:,1] = random.randint(0, 255)
bgr_img[:,:,2] = random.randint(0, 255)
cv2.imshow('bgr_img',bgr_img)
cv2.waitKey(0)
