# -*- coding: utf-8 -*-

import os
import sys
import xml.dom.minidom
from prettytable import PrettyTable

def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []

def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

anno_path = sys.argv[1]

if not os.path.exists(sys.argv[1]):
    print("cannot find such directory: " + sys.argv[1])
    exit()


result = os.walk(anno_path)
name_set = set()
name_num_dict = {}


for a in result:
    for file_x in a[2]:
        print("start scanning file: " + file_x)
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


class_num = 'class number: '+str(len(name_set))

print("scanning finished" + '\n' + class_num)

name_num_list = sorted(name_num_dict.items(), key = lambda d:d[0])

table = PrettyTable(["Class","Number"])
table.align["Class"] = "l"
table.padding_width = 1
for tup in name_num_list:
	table.add_row([tup[0], tup[1]])

print(table)

#print(name_num_dirc)