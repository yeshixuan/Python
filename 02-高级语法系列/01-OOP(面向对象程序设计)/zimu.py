#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:32
# @Author  : Yebiyun
# @Site    : 
# @File    : zimu.py
# @Software: PyCharm
import random as ra
class Game_zimu(object):
    def __init__(self, strs):
        self.strs = strs
        self.user()
    def user(self):
        if self.strs == "a":
            self.printA()
        if self.strs == "b":
            self.printB()
        if self.strs == "c":
            self.printC()
        if self.strs == "d":
            self.printD()
    def printA(self):
        for i in range(5):
            for j in range(4-i):
                print(" ", end="")
            for k in range(i+1):
                if i in [3,4] and (0 < k < i):
                    print(" ", end = " ")
                else:
                    print("*", end=" ")
            print()
    def printB(self):
        for i in range(7):
            for j in range(4):
                if (i in [0,3,6] and j in [0,1,2]) or (i in [1,2,4,5] and j in [0,3] ):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    def printC(self):
        for i in range(4):
            for j in range(4):
                if (i in [0,3] and j in [1,2,3]) or (i in [1,2] and j == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    def printD(self):
        for i in range(4):
            for j in range(4):
                if (i in [0,3] and j in [0,1,2]) or (i in [1,2] and j in [0,3]):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
def main():
    while True:
        strs = input("请输入您要打印的字母（a-z）,退出游戏请输（0）：")
        if ((len(strs) > 1) or (ord(strs) not in [i for i in range(97,123)])) and (strs != "0"):
            print("输入格式错误，请重新输入！")
        elif strs == "0":
            break
        else:
            p = Game_zimu(strs)

if __name__ == '__main__':
    main()

