#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 21:19
# @Author  : Yebiyun
# @Site    : 
# @File    : math模块相关函数.py
# @Software: PyCharm

# ascii转数字
print(ord("A"))
print(ord("z"))

# 数字转asciil码
print(chr(118))
import math
# print(math) math是数学模块
# Ctrl+/ 会注释掉
'''
# celi()  向上取整操作
print(math.ceil(5.1))
print(math.ceil(5.99))

# floor() 向下取整
print(math.floor(5.01))
print(math.floor(5.99))

# 查看系统保留关键字，不可以用来当做变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入操作 python的内置函数
print(round(5.01))
print(round(5.5))

# sqrt() 开平方 返回浮点数
print(math.sqrt(16))

# pow() ，返回整数 幂运算,计算一个数的几次方，有两个参数，第一个是底数，第二个是指数
# math.pow() 返回的是浮点数
print(pow(2,3)) #等于print(2**3)
#print(math.pow(3,3))

# fabs() 对一个数值获取它的绝对值， 返回的也是浮点数
print(math.fabs(-1))
print(math.fabs(3))

# abs() 获取绝对值操作 ，不是数学模块当中的，是Python内置函数,返回值由本身类型而定
print(abs(-9))

# fsum() 对整个序列求和
print(math.fsum([1,2,3,5,6]))
# sum() python内置求和
print(sum([1,2,3,5,6]))

# math.modf() 将一个浮点数拆分为整数部分和小数部分，返回一个元组
print(math.modf(4.5))#小数在前，整数在后，都是浮点数
print(math.modf(0))
print(math.modf(3))
help(math.modf)

# copysign() 将第二个数的符号（正负号）传递给第一个数
print(math.copysign(2,-3))
print(math.copysign(-3,2))

# 打印自然对数e和π的值
print(math.e)
print(math.pi)
'''
import random
# random() 获取0-1之间的随机小数 包含0不包含1
#for i in range(10):
    # print(random.random())
    # 随机指定开始和结束之间的整数值
    #print(random.randint(1,4))
    # random.randrange() 获取指定开始和结束之间的值，可以指定间隔纸
    # print(random.randrange(1,9,2))

'''
# choice() 随机获取列表中的值
print(random.choice([1,2,3,5]))
# shuffle() 随机打乱序列 返回值是None
list1 = [1,2,3,4,5,6,6]
print(list1)
random.shuffle(list1)
print(list1)

for i in range(4):
    # uniform（） 随机获取指定范围内的值（包括小数
    print(random.uniform(1, 9))
'''
