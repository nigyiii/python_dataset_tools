import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import sys
import os
import traceback
from tqdm import tqdm
    
from  albumentations  import (
    JpegCompression, RGBShift, RandomGamma, HorizontalFlip, CenterCrop, 
    IAAPerspective, ShiftScaleRotate, CLAHE, RandomRotate90, ToGray,
    Transpose, ShiftScaleRotate, Blur, OpticalDistortion, GridDistortion, HueSaturationValue,
    IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, IAAPiecewiseAffine,
    IAASharpen, IAAEmboss, RandomContrast, RandomBrightness, Flip, OneOf, Compose
) # 图像变换函数

imgdir = '/Users/ngy/data/flag/flag_add/roi'
savedir = '/Users/ngy/data/flag/flag_add/aug'

for path in tqdm(os.listdir(imgdir)):
    try:
        img_path = os.path.join(imgdir, path)
        image = cv2.imread(img_path, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        w = image.shape[1]
        h = image.shape[0]
            
        def strong_aug(w, h, p=1):
            return Compose([
                #RandomRotate90(),
                #Flip(),
                HorizontalFlip(p=0.5),
                #Rotate(limit=30, p=0.5)
                #Transpose(),
                #IAAAdditiveGaussianNoise(),
                #GaussNoise(var_limit=(30, 80.0), mean=0, always_apply=False, p=0.5),
                JpegCompression(quality_lower=3, quality_upper=100, p=0.5),
                OneOf([
                    MotionBlur(),
                    MedianBlur(blur_limit=10),
                    Blur(blur_limit=10)
                ], p=1),
                ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=90, p=.8),
                RGBShift(r_shift_limit=20, g_shift_limit=20, b_shift_limit=20, p=0.5),
                #RandomGamma(gamma_limit=30, p=1),
                #ToGray(p=0.1),
                #CenterCrop(height=random.randint(int(h*0.7), int(h*0.9)), width=random.randint(int(w*0.7), int(w*0.9)), p=0.5),
                CLAHE(clip_limit=2),
                IAASharpen(),
                #Flip(p=0.5),
                #IAAEmboss(),
                #RandomContrast(),
                RandomBrightness(),
                #HueSaturationValue(hue_shift_limit=172, sat_shift_limit=20, val_shift_limit=27, p=0.5)
                #HueSaturationValue(p=0.3),
            ], p=p)
            
        aug  = strong_aug(w, h, p=1)

        for i in range(1, 11):
            img_aug = aug(image=image)['image']
            img_aug = cv2.cvtColor(img_aug, cv2.COLOR_RGB2BGR)
            #print(os.path.join(savedir, os.path.splitext(path)[0] + '_' + str(i) + os.path.splitext(path)[1]))
            cv2.imwrite(os.path.join(savedir, os.path.splitext(path)[0] + '_' + str(i) + os.path.splitext(path)[1]), img_aug)
    except Exception as e:
        print(e)
        print(traceback.format_exc())


