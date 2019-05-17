import cv2
import os
import os.path
import xml.dom.minidom


def getXmlNode(node, name):
    return node.getElementsByTagName(name) if node else []


def getNodeValue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''


data_dir = '/Users/ngy/Desktop/data/logo/rongwei_shuffle/shuffled'
img_dir = data_dir + '/images'
xml_dir = data_dir + '/xml'
output_dir = data_dir + '/img_box'

ImageNames = os.listdir(img_dir)

for img_file in ImageNames:
    print(img_file)
    if img_file[-4:] == '.jpg':
        img = cv2.imread(img_dir + '/' + img_file)

        xml_file = img_file[:-4] + '.xml'
        dom = xml.dom.minidom.parse(os.path.join(xml_dir, xml_file))
        root = dom.documentElement
        objects = getXmlNode(root, "object")

        for object in objects:
            xmin = int(float(getNodeValue(getXmlNode(object, "xmin")[0])))
            ymin = int(float(getNodeValue(getXmlNode(object, "ymin")[0])))
            xmax = int(float(getNodeValue(getXmlNode(object, "xmax")[0])))
            ymax = int(float(getNodeValue(getXmlNode(object, "ymax")[0])))
            print(xmin, ymin, xmax, ymax)

        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        cv2.imwrite(output_dir + '/' + img_file, img)
