# -*- coding: utf-8 -*-

# coding=utf-8
import os
import os.path
import xml.dom.minidom
import shutil

_dic = {
'p0400':'rongwei',
'p0600':'meizanchen',
'p0610':'aitamei',
'p0611':'yapei',
'p0612':'liangpinpuzi',
'p0613':'laiyifen',
'p0614':'sinian',
'p0615':'sanzhisongshu',
'p0616':'Jeep',
'p0620':'pufa',
'p0621':'huaxia',
'p0622':'zhonghang',
'p0623':'zhaohang',
'p0624':'jiaotong',
'p0625':'gonghang',
'p0626':'nonghang',
'p0627':'jianhang',
'p0630':'fedex',
'p0631':'ups',
'p0632':'jingdong',
'p0633':'jingdong-dog',
'p0634':'tmall',
'p0635':'tmall-cat',
'p0636':'weipinhui',
'p0637':'xiaohongshu',
'p0638':'wangyiyanxuan',
'p0639':'wangyikaola',
'p0640':'shunfeng',
'p0641':'baiwei',
'p0642':'qingdao',
'p0643':'jiangxiaobai'
}

for i in range(0, 1):
#for _dir in os.listdir('/Users/ngy/data/double11/images'):
#获得文件夹中所有文件
    #base_path = '/Users/ngy/data/double11/images/' + _dir
    base_path = '/Users/ngy/data/logov1/VOC2007'
    xml_path = base_path + '/Annotations'
    img_path = base_path + '/JPEGImages'
    FileNames = os.listdir(xml_path)
    shuffled_path = base_path + '/shuffled'
    shuffled_xml_path = shuffled_path + '/Annotations'
    shuffled_img_path = shuffled_path + '/JPEGImages'
    #FileNames = os.listdir(shuffled_xml_path)
    num = 0

    for path in shuffled_path, shuffled_xml_path, shuffled_img_path:
        if not os.path.exists(path):
            os.makedirs(path)


    def getXmlNode(node, name):
        return node.getElementsByTagName(name) if node else []


    #old_name = _dir
    #new_name = _dic[_dir]
    FileNames = os.listdir(xml_path)

    for file_name in FileNames:
        print(file_name)
        if file_name[-4:] == '.xml':
            old_name = file_name.split('_')[0]
            new_name = _dic[old_name]
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
                #if name[0].firstChild.data == old_name:
                    #name[0].firstChild.data = new_name
                this_old_name = name[0].firstChild.data
                name[0].firstChild.data = _dic[this_old_name]
            #将修改后的xml文件保存
            with open(os.path.join(shuffled_xml_path, serial + '.xml'), 'w') as fh:
                dom.writexml(fh)
                #print("name \'" + old_name + "\' replaced by \'" + new_name + "\' in " + file_name)
                print("name \'" + this_old_name + "\' replaced by \'" + name[0].firstChild.data + "\' in " + file_name)

            num += 1


    print(str(num) + ' files processed')