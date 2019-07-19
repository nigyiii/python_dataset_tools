# -*- coding: utf-8 -*-

import os
import shutil
import random

xml_dir = '/Users/ngy/data/person/del'
img_dir = '/Users/ngy/data/person/img'
save_xml_dir = '/Users/ngy/data/person_400/xml'
save_img_dir = '/Users/ngy/data/person_400/img'

Names = random.sample(os.listdir(xml_dir), 400)
print len(Names)

for dir in save_xml_dir, save_img_dir:
    if not os.path.exists(dir):
        os.makedirs(dir)

for xml_file in Names:
    if xml_file[-4:] == '.xml':
        print 'selecting ' + xml_file
        img_file = xml_file[:-4] + '.jpg'
        shutil.copy(os.path.join(xml_dir, xml_file), os.path.join(save_xml_dir, xml_file))
        shutil.copy(os.path.join(img_dir, img_file), os.path.join(save_img_dir, img_file))