import os
import sys
import shutil
import random
from tqdm import tqdm

srcdir = '/Users/ngy/data/flag/roi'
filelist = os.listdir(srcdir)
trainlist = random.sample(filelist, int(len(filelist)*0.98))
vallist = list(set(filelist) - set(trainlist))
traindir = '/Users/ngy/data/flag/train'
valdir = '/Users/ngy/data/flag/val'

for file in tqdm(trainlist):
    #print(file)
    index = file.split('_')[0]
    #print(traindir, index)
    clsdir = os.path.join(traindir, str(index))
    if not os.path.exists(clsdir):
        os.makedirs(clsdir)
    #print(os.path.join(traindir, file), os.path.join(clsdir, file))
    shutil.move(os.path.join(srcdir, file), os.path.join(clsdir, file))

for file in tqdm(vallist):
    #print(file)
    index = file.split('_')[0]
    #print(traindir, index)
    clsdir = os.path.join(valdir, str(index))
    if not os.path.exists(clsdir):
        os.makedirs(clsdir)
    #print(os.path.join(traindir, file), os.path.join(clsdir, file))
    shutil.move(os.path.join(srcdir, file), os.path.join(clsdir, file))

'''
for file in tqdm(os.listdir(traindir)):
    #print(file)
    index = file.split('_')[0]
    #print(traindir, index)
    clsdir = os.path.join(traindir, str(index))
    if not os.path.exists(clsdir):
        os.makedirs(clsdir)
    #print(os.path.join(traindir, file), os.path.join(clsdir, file))
    shutil.move(os.path.join(traindir, file), os.path.join(clsdir, file))

for file in tqdm(os.listdir(valdir)):
    index = file.split('_')[0]
    clsdir = os.path.join(valdir, str(index))
    if not os.path.exists(clsdir):
        os.makedirs(clsdir)
    shutil.move(os.path.join(valdir, file), os.path.join(clsdir, file))
'''