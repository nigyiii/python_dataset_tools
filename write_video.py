# -*- coding: utf-8 -*-

# coding=utf-8

import cv2
import os
import sys
import random
import shutil

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
writer = cv2.VideoWriter('/Users/ngy/modify/testcolorbar.mp4', fourcc, fps, (800,450))
for img_dir in '/Users/ngy/data/colorbar/n', '/Users/ngy/data/colorbar/p':
    for img_path in os.listdir(img_dir):
        img = cv2.imread(os.path.join(img_dir, img_path))
        img = cv2.resize(img, (800,450))
        writer.write(img)

writer.release()