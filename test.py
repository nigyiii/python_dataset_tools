from label_utils import count_label, rename_label, find_label
import os
import chardet
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


def main():

    table, clen = count_label('/Users/ngy/data/VOC2007/Annotations')
    print(table)
    print(clen)
main()