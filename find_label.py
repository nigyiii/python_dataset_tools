# -*- coding: utf-8 -*-

import cv2
import os
import os.path
import xml.dom.minidom
import shutil


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''


data_dir = '/Users/ngy/data/logo_mangguo/pad_aug/VOCdevkit/VOC2007'
xml_dir = data_dir + '/Annotations'
img_dir = data_dir + '/JPEGImages'
save_img_dir = '/Users/ngy/data/logo_mangguo/souhu_huyou/img'
save_xml_dir = '/Users/ngy/data/logo_mangguo/souhu_huyou/xml'

for _path in save_xml_dir, save_img_dir:
    if not os.path.exists(_path):
        os.makedirs(_path)

ImageNames = os.listdir(img_dir)
ImageNames.sort()

for img_file in ImageNames:
    if img_file[-4:] == '.jpg':

        xml_file = img_file[:-4] + '.xml'
        dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
        root = dom.documentElement
        objects = getXmlNode(root, "object")

        for object in objects:
            xmin = int(float(getNodeValue(getXmlNode(object, "xmin")[0])))
            ymin = int(float(getNodeValue(getXmlNode(object, "ymin")[0])))
            xmax = int(float(getNodeValue(getXmlNode(object, "xmax")[0])))
            ymax = int(float(getNodeValue(getXmlNode(object, "ymax")[0])))
            label = getNodeValue(getXmlNode(object, "name")[0])
            if label == 'souhu_huyou':
                shutil.copy(img_dir + '/' + img_file, save_img_dir + '/' + img_file)
                shutil.copy(xml_dir + '/' + xml_file, save_xml_dir + '/' + xml_file)
                print('find label in ' + img_file)
                break