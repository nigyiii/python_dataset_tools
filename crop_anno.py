# -*- coding: utf-8 -*-

# coding=utf-8
import os
import os.path
import xml.dom.minidom
import shutil
import cv2
import random
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#获得文件夹中所有文件
base_path = '/Users/ngy/data/test'
xml_path = base_path + '/xml'
img_path = base_path + '/img'
FileNames = os.listdir(xml_path)
shuffled_path = base_path + '/aug'
shuffled_xml_path = shuffled_path + '/xml'
shuffled_img_path = shuffled_path + '/img'
#FileNames = os.listdir(shuffled_xml_path)
num = 0

for path in shuffled_path, shuffled_xml_path, shuffled_img_path:
    if not os.path.exists(path):
        os.makedirs(path)


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''



for file_name in FileNames:
    print(file_name)
    if file_name[-4:] == '.xml':
        for i in range(0, 10):
            print i
            img = cv2.imread(img_path + '/' + file_name[:-4] + '.jpg')
            #print img_path + '/' + file_name[:-4] + '.jpg'
            wh_ratio = float(img.shape[1]) / float(img.shape[0])
            #print 'wh_ratio:', wh_ratio
            crop_wh_ratio = random.uniform(0.5, 1.5) * wh_ratio
            #print 'crop_wh_ratio:', crop_wh_ratio
            crop_height = random.randint(int(float(img.shape[0]) * 0.2), int(float(img.shape[0]) * 1.2))
            crop_width = int(crop_height * crop_wh_ratio)
            #print 'crop_width, crop_height:', crop_width, crop_height
            img_crop = cv2.resize(img, (crop_width, crop_height))

            mask = np.ones((crop_height, crop_width), dtype=np.uint8)
            bgr_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            bgr_mask[:,:,0] = random.randint(0, 255)
            bgr_mask[:,:,1] = random.randint(0, 255)
            bgr_mask[:,:,2] = random.randint(0, 255)

            img_crop = cv2.addWeighted(img_crop, 0.5, bgr_mask, 0.5, 0)
            cv2.imwrite(os.path.join(shuffled_img_path, file_name[:-4] + '_' + str(i) + '.jpg'), img_crop)
            w_ratio = float(crop_width) / float(img.shape[1])
            h_ratio = float(crop_height) / float(img.shape[0])
            #print 'w_ratio, h_ratio:', w_ratio, h_ratio
            #读取xml文件
            dom = xml.dom.minidom.parse(os.path.join(xml_path,file_name))
            root = dom.documentElement
            #filename = getXmlNode(root, "filename")

            width = getXmlNode(root, 'width')[0]
            width.firstChild.data = crop_width
            height = getXmlNode(root, 'height')[0]
            height.firstChild.data = crop_height

            objects = getXmlNode(root, "object")

            for object in objects:
                xmin = int(float(getNodeValue(getXmlNode(object, "xmin")[0])))
                ymin = int(float(getNodeValue(getXmlNode(object, "ymin")[0])))
                xmax = int(float(getNodeValue(getXmlNode(object, "xmax")[0])))
                ymax = int(float(getNodeValue(getXmlNode(object, "ymax")[0])))
                
                _xmin = getXmlNode(object, "xmin")[0]
                _ymin = getXmlNode(object, "ymin")[0]
                _xmax = getXmlNode(object, "xmax")[0]
                _ymax = getXmlNode(object, "ymax")[0]
                _xmin.firstChild.data = int(xmin * w_ratio)
                _ymin.firstChild.data = int(ymin * h_ratio)
                _xmax.firstChild.data = int(xmax * w_ratio)
                _ymax.firstChild.data = int(ymax * h_ratio)
                #print '_xmin, _ymin, _xmax, _ymax:', int(xmin * w_ratio), int(ymin * h_ratio), int(xmax * w_ratio), int(ymax * h_ratio)
            #将修改后的xml文件保存
            with open(os.path.join(shuffled_xml_path, file_name[:-4] + '_' + str(i) + '.xml'), 'w') as fh:
                dom.writexml(fh)
         
        num += 1


print(str(num) + ' files processed')