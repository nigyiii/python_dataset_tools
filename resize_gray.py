# -*- coding: utf-8 -*-

import cv2
import os

base_dir = '/Users/ngy/data/jj'
input_dir = base_dir + '/roi'
output_dir = base_dir + '/gray'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ImageNames = os.listdir(input_dir)

for img_file in ImageNames:
    print(img_file)
    if img_file[-4:] == '.jpg':
        print 'resize', img_file
        img = cv2.imread(input_dir + '/' + img_file)
        img_crop = cv2.resize(img, (40, 40))
        img_gray = cv2.cvtColor(img_crop, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(output_dir + '/' + img_file, img_gray)