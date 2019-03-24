#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 21:45
# @Author  : Yebiyun
# @Site    : 
# @File    : 1.py
# @Software: PyCharm
def file_company(f1, f2):
    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()

        count += 1
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()

    return differ


def f_isexists(name):
    while True:
        file = input("请输入需要比较的第{}个文件名：".format(name))
        try:
            f = open(file, encoding="utf-8")
        except:
            print("该文件不存在，请重新输入！")
        else:
            f = open(file, encoding="utf-8")
            break
    return f


f1 = f_isexists("一")
f2 = f_isexists("二")

if f1.read().count("\n") < f2.read().count("\n"):
    differ = file_company(f2, f1)
    print("1")
else:
    differ = file_company(f1, f2)
    print("2")

if len(differ) == 0:
    print("两个文件完全相同")
else:
    print("两个文件有{}行不同".format(len(differ)))
    for s in differ:
        print("第{}行不同".format(s))