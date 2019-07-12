# -*- coding: utf-8 -*-

import cv2
import os
import os.path
import xml.dom.minidom


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''


data_dir = '/Users/ngy/data/jj'
img_dir = data_dir + '/img'
xml_dir = data_dir + '/xml'
output_dir = data_dir + '/pos'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ImageNames = os.listdir(img_dir)

for img_file in ImageNames:
    print(img_file)
    if img_file[-4:] == '.jpg':
        img = cv2.imread(img_dir + '/' + img_file)
        #h = img.shape[0]

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
            print(xmin, ymin, xmax, ymax, label)
            img_crop = img[ymin:ymax, xmin:xmax]

        cv2.imwrite(output_dir + '/' + img_file, img_crop)