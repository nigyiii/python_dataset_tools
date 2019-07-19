# -*- coding: utf-8 -*-

import cv2
import os
import os.path
import xml.dom.minidom
import shutil
import re


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''


xml_dir = '/Users/ngy/data/person2/xml'
tmp_dir = '/Users/ngy/data/person2/tmp'
del_dir = '/Users/ngy/data/person2/del'

Names = os.listdir(xml_dir)
Names.sort()

for dir in tmp_dir, del_dir:
    if not os.path.exists(dir):
        os.makedirs(dir)

for xml_file in Names:
    if xml_file[-4:] == '.xml':
        print 'processing ' + xml_file
        dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
        root = dom.documentElement
        objects = getXmlNode(root, "object")

        for object in objects:
            label = getNodeValue(getXmlNode(object, "name")[0])
            if not label == 'person':
                object.parentNode.removeChild(object)

        with open(os.path.join(tmp_dir, xml_file), 'w') as fh:
            dom.writexml(fh)
        
        w = open(os.path.join(del_dir, xml_file),'w')
        empty=re.compile('^\s*$')
        for line in open(os.path.join(tmp_dir, xml_file), 'r').readlines():
            if empty.match(line):
                continue
            else: 
                w.write(line)

shutil.rmtree(tmp_dir)





