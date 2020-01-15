# -*- coding: utf-8 -*-

import os
import sys
import xml.dom.minidom
from prettytable import PrettyTable
import re
import shutil
import traceback

def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []

def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''

def count_label(anno_path):
    if not os.path.exists(anno_path):
        print("cannot find such directory: " + anno_path)
        exit()
    clen = len(os.listdir(anno_path))
    result = os.walk(anno_path)
    name_set = set()
    name_num_dict = {}
    #print(result)
    for a in result:
        #print(a)
        for file_x in a[2]:
            #print(file_x)
            try:
                #print("start scanning file: " + file_x)
                file_path = os.path.join(anno_path, file_x)
                dom = xml.dom.minidom.parse(file_path)
                root = dom.documentElement
                filename = root.getElementsByTagName("filename")
                filename = getNodeValue(filename[0])
                node = getXmlNode(root, "object")
                list_tem = []

                for node_tem in node:
                    name = getXmlNode(node_tem, "name")
                    name = getNodeValue(name[0])
                    name_set.add(name)
         
                    if name in name_num_dict.keys():
                        name_num_dict[name] += 1
                    else:
                        name_num_dict[name] = 1
            except Exception as e:
                print(e)        

    class_num = 'class number: '+str(len(name_set))
    #print("scanning finished" + '\n' + class_num)
    name_num_list = sorted(name_num_dict.items(), key = lambda d:d[0])
    table = PrettyTable(["Class","Number"])
    table.align["Class"] = "l"
    table.padding_width = 1
    for tup in name_num_list:
    	table.add_row([tup[0], tup[1]])

    return table, clen


def find_label(xml_dir, target):

    XmlNames = os.listdir(xml_dir)
    
    XmlNames.sort()
    foundlist = []

    for xml_file in XmlNames:
        try:
            dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
            root = dom.documentElement
            objects = getXmlNode(root, "object")

            for object in objects:
                label = getNodeValue(getXmlNode(object, "name")[0])
                if label == target:
                    foundlist.append(xml_file)
                    break
        except Exception as e:
            print(e)
            print(traceback.format_exc())

    return foundlist


def remove_label(srcdir, dstdir, target):
    xml_dir = srcdir
    tmp_dir = os.path.join(dstdir, 'temp')
    del_dir = dstdir

    Names = os.listdir(xml_dir)
    Names.sort()

    for dir in tmp_dir, del_dir:
        if not os.path.exists(dir):
            os.makedirs(dir)
 
    for xml_file in Names:
        try:
            #print('processing ' + xml_file)
            dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
            root = dom.documentElement
            objects = getXmlNode(root, "object")
            for object in objects:
                label = getNodeValue(getXmlNode(object, "name")[0])
                if label == target:
                    object.parentNode.removeChild(object)

            with open(os.path.join(del_dir, xml_file), 'w') as fh:
                dom.writexml(fh)
            
            #w = open(os.path.join(del_dir, xml_file),'w')
            #empty=re.compile('^\s*$')
            #for line in open(os.path.join(tmp_dir, xml_file), 'r').readlines():
            #    if empty.match(line):
            #        continue
            #    else: 
            #        w.write(line)
        except Exception as e:
            print(e)
            print(traceback.format_exc())

    shutil.rmtree(tmp_dir)


def rename_label(xml_path, dst_path, origin_name, new_name):
    shuffled_xml_path = dst_path
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    FileNames = os.listdir(xml_path)

    for file_name in FileNames:
        try:
            #print(file_name)
            old_name = file_name.split('_')[0] 
            dom = xml.dom.minidom.parse(os.path.join(xml_path,file_name))
            root = dom.documentElement
            node = getXmlNode(root, "object") 
            for node_tem in node:
                name = getXmlNode(node_tem, "name")
                if name[0].firstChild.data == origin_name:
                    name[0].firstChild.data = new_name

            with open(os.path.join(shuffled_xml_path, file_name), 'w') as fh:
                dom.writexml(fh)
        except Exception as e:
            print(e)
            print(traceback.format_exc())

if __name__ == '__main__':
    rename_label('/Users/ngy/data/flag/p', '/Users/ngy/data/flag/p', '0', 'xx')