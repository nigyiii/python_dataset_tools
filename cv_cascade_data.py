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
img_dir = data_dir + '/gray'
xml_dir = data_dir + '/xml'

info = open(data_dir + '/info.txt', 'w')

ImageNames = os.listdir(img_dir)
ImageNames.sort()

for img_file in ImageNames:
    print(img_file)
    if img_file[-4:] == '.jpg':
        #img = cv2.imread(img_dir + '/' + img_file)
        #h = img.shape[0]
        info.write(img_dir[-4:] + '/' + img_file + ' 1 0 0 40 40\n')


        #xml_file = img_file[:-4] + '.xml'
        #dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
        #root = dom.documentElement
        #objects = getXmlNode(root, "object")
        #info.write(img_dir[-3:] + '/' + img_file + ' ' + str(len(objects)))
'''
        for object in objects:
            xmin = int(float(getNodeValue(getXmlNode(object, "xmin")[0])))
            ymin = int(float(getNodeValue(getXmlNode(object, "ymin")[0])))
            xmax = int(float(getNodeValue(getXmlNode(object, "xmax")[0])))
            ymax = int(float(getNodeValue(getXmlNode(object, "ymax")[0])))
            label = getNodeValue(getXmlNode(object, "name")[0])
            info.write(' ' + str(xmin) + ' ' + str(ymin) + ' ' + str(xmax - xmin) + ' ' + str(ymax - ymin))
            print(xmin, ymin, xmax, ymax, label)

        info.write('\n')
'''
info.close()

            