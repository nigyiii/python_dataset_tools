# -*- coding: utf-8 -*-

# coding=utf-8
import os
import os.path
import xml.dom.minidom
import shutil

#获得文件夹中所有文件
FindPath = '/Users/ngy/Desktop/data/logo/rongwei_shuffle/images/500/labels'
FileNames = os.listdir(FindPath)
xml_path = '/Users/ngy/Desktop/data/logo/rongwei_shuffle/shuffled/xml'
num = 0


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


for file_name in FileNames:
    print(file_name)
    if file_name[-4:] == '.xml':
        #读取xml文件
        dom = xml.dom.minidom.parse(os.path.join(FindPath,file_name))
        root = dom.documentElement
        filename = getXmlNode(root, "filename")
        serial = 'p0400_' + str(num + 1).zfill(4)
        shutil.copy('/Users/ngy/Desktop/data/logo/rongwei_shuffle/images/500/images/' + filename[0].firstChild.data,
            '/Users/ngy/Desktop/data/logo/rongwei_shuffle/shuffled/images/' + serial + '.jpg')
        filename[0].firstChild.data = serial + '.jpg'
        node = getXmlNode(root, "object")
        # 获取标签对name之间的值   
        for node_tem in node:
            name = getXmlNode(node_tem, "name")
            #for i in range(len(name)):
            #print name[i].firstChild.data
            if name[0].firstChild.data == '500':
                name[0].firstChild.data = 'p0400'
        #将修改后的xml文件保存
        with open(os.path.join(xml_path, serial + '.xml'), 'w') as fh:
            dom.writexml(fh)
            print("name \'500\' replaced by \'p0400\' in " + file_name)

        num += 1


print(str(num) + ' files processed')