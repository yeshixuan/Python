import xml.etree.ElementTree as et

stu = et.Element("Student1")

name = et.SubElement(stu, "Name")
name.attrib = {"lang","en"}
name.text = "maozexi"


age = et.SubElement(stu, "Age")
age.text = 15

et.dump(stu)