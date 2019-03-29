import xml.dom.minidom
# 负责解析xml文件
from xml.dom.minidom import parse

# 使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("student.xml")
# 得到文档对象
doc = DOMTree.documentElement

# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("--------Node:{}------".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                # data是文本节点的一个属性，表示它的值
                print("Name: {}".format(child.childNodes[0].data))
            if child.nodeName == "Mobile":
                print("Mobile: {}".format(child.childNodes[0].data))
            if child.nodeName == "Age":
                print("Age: {}".format(child.childNodes[0].data))
                if child.hasAttribute("Detail"):
                    print("Age-Detail: {}".format(child.getAttribute("Detail")))