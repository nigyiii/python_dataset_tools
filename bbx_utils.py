# -*- coding: utf-8 -*-

import cv2
import os
import os.path
import xml.dom.minidom
import time
import sys


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''


def crop_bbx(img_dir, xml_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ImageNames = os.listdir(img_dir)

    for img_file in ImageNames:
        #print(img_file)
        try:
            img = cv2.imread(img_dir + '/' + img_file)
            #h = img.shape[0]

            xml_file = img_file[:-4] + '.xml'
            dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
            root = dom.documentElement
            objects = getXmlNode(root, "object")

            for object in objects:
                xmin = max(int(float(getNodeValue(getXmlNode(object, "xmin")[0]))), 0)
                ymin = max(int(float(getNodeValue(getXmlNode(object, "ymin")[0]))), 0)
                xmax = min(int(float(getNodeValue(getXmlNode(object, "xmax")[0]))), img.shape[1])
                ymax = min(int(float(getNodeValue(getXmlNode(object, "ymax")[0]))), img.shape[0])
                label = getNodeValue(getXmlNode(object, "name")[0])
                #print(xmin, ymin, xmax, ymax, label)
                img_roi = img[ymin:ymax, xmin:xmax]
                if img_roi.size == 0:
                    continue
                #img_crop = cv2.resize(img_roi, (64, 64))
                cv2.imwrite(output_dir + '/' + str(int(label)) + '_' + str(time.time()).replace('.', '') + '.jpg', img_roi)
        except Exception as e:
            print(e)

def draw_bbx(img_dir, xml_dir, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ImageNames = os.listdir(img_dir)

    for img_file in ImageNames:
        try:
            #print(img_file)
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
                #print(xmin, ymin, xmax, ymax, label)
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                cv2.putText(img, label, (xmin, ymin - 2), 0, 1, (0, 255, 0), 2)

            cv2.imwrite(output_dir + '/' + img_file, img)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    draw_bbx('/Users/ngy/data/flag/VOCdevkit/VOC2007/JPEGImages', '/Users/ngy/data/flag/VOCdevkit/VOC2007/Annotations', '/Users/ngy/data/test/aug')