# -*- coding: utf-8 -*-

# coding=utf-8
import os
import os.path
import xml.dom.minidom
import shutil

#获得文件夹中所有文件
base_path = '/Users/ngy/data/temp/download/images/632'
xml_path = base_path + '/labels'
img_path = base_path + '/images'
FileNames = os.listdir(xml_path)
shuffled_path = base_path + '/shuffled'
shuffled_xml_path = shuffled_path + '/xml'
shuffled_img_path = shuffled_path + '/img'
#FileNames = os.listdir(shuffled_xml_path)
num = 0

for path in shuffled_path, shuffled_xml_path, shuffled_img_path:
    if not os.path.exists(path):
        os.makedirs(path)


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


old_name = '632'
new_name = 'p0632'


for file_name in FileNames:
    print(file_name)
    if file_name[-4:] == '.xml':
        #读取xml文件
        dom = xml.dom.minidom.parse(os.path.join(xml_path,file_name))
        root = dom.documentElement
        filename = getXmlNode(root, "filename")
        serial = new_name + '_' + str(num + 1).zfill(4)
        shutil.copy(img_path + '/' + filename[0].firstChild.data,
            shuffled_img_path + '/' + serial + '.jpg')
        filename[0].firstChild.data = serial + '.jpg'
        node = getXmlNode(root, "object")
        # 获取标签对name之间的值   
        for node_tem in node:
            name = getXmlNode(node_tem, "name")
            #for i in range(len(name)):
            #print name[i].firstChild.data
            if name[0].firstChild.data == old_name:
                name[0].firstChild.data = new_name
        #将修改后的xml文件保存
        with open(os.path.join(shuffled_xml_path, serial + '.xml'), 'w') as fh:
            dom.writexml(fh)
            print("name \'" + old_name + "\' replaced by \'" + new_name + "\' in " + file_name)

        num += 1


print(str(num) + ' files processed')