# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # print(root)
        print(root.find('filename').text)
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text), #width
                     int(root.find('size')[1].text), #height
                     member.find('name').text,
                     int(member.find('bndbox')[0].text),
                     int(member.find('bndbox')[1].text),
                     int(member.find('bndbox')[2].text),
                     int(member.find('bndbox')[3].text),
                     )
            print value
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train','test','validation']:
        xml_path = os.path.join('/Users/ngy/data/jj_person', 'Annotations/{}'.format(directory))
        xml_df = xml_to_csv(xml_path)
        xml_df.to_csv('/Users/ngy/data/jj_person/csv/jj_{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')

main()