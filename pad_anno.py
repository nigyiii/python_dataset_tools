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
base_path = '/Users/ngy/data/logo_mangguo'
xml_path = base_path + '/xml'
img_path = base_path + '/img'
FileNames = os.listdir(xml_path)
shuffled_path = base_path + '/pad_aug'
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
        for i in range(0, 3):
            print i
            img = cv2.imread(img_path + '/' + file_name[:-4] + '.jpg')
            #print img_path + '/' + file_name[:-4] + '.jpg'

            pad_up = random.randint(int(float(img.shape[0]) * 0.25), int(float(img.shape[0]) * 0.5))
            pad_down = random.randint(int(float(img.shape[1]) * 0.25), int(float(img.shape[1]) * 0.5))
            pad_left = random.randint(int(float(img.shape[0]) * 0.25), int(float(img.shape[0]) * 0.5))
            pad_right = random.randint(int(float(img.shape[1]) * 0.25), int(float(img.shape[1]) * 0.5))
            #img_pad = cv2.copyMakeBorder(img, pad_up, pad_down, pad_left, pad_right, cv2.BORDER_CONSTANT, value = [0, 0, 0])
            #img_pad = cv2.copyMakeBorder(img, pad_up, pad_down, pad_left, pad_right, cv2.BORDER_REPLICATE)
            #img_pad = cv2.copyMakeBorder(img, pad_up, pad_down, pad_left, pad_right, cv2.BORDER_REFLECT)
            #img_pad = cv2.copyMakeBorder(img, pad_up, pad_down, pad_left, pad_right, cv2.BORDER_REFLECT_101)
            img_pad = cv2.copyMakeBorder(img, pad_up, pad_down, pad_left, pad_right, cv2.BORDER_WRAP)
            #print 'img_pad', img_pad.shape

            #读取xml文件
            dom = xml.dom.minidom.parse(os.path.join(xml_path,file_name))
            root = dom.documentElement

            width = getXmlNode(root, 'width')[0]
            width.firstChild.data = img_pad.shape[1]
            height = getXmlNode(root, 'height')[0]
            height.firstChild.data = img_pad.shape[0]

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

                _xmin.firstChild.data = xmin + pad_left
                _ymin.firstChild.data = ymin + pad_up
                _xmax.firstChild.data = xmax + pad_left
                _ymax.firstChild.data = ymax + pad_up
            
            #将修改后的文件保存
            new_name = file_name[:-4] + '_pad_' + str(i).zfill(3)
            cv2.imwrite(os.path.join(shuffled_img_path, new_name + '.jpg'), img_pad)
            with open(os.path.join(shuffled_xml_path, new_name + '.xml'), 'w') as fh:
                dom.writexml(fh)
                     
        num += 1


print(str(num) + ' files processed')