#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 21:16
# @Author  : Yebiyun
# @Site    : 
# @File    : my_game.py
# @Software: PyCharm
import zimu as z
import rand_math面向对象练习 as n

def main():
    while True:
        choice_str = input("请选择要玩的游戏，字母打印游戏选择1，猜数字选择2，退出游戏选择0，请输入选择（0/1/2）:")
        if choice_str not in ["0","1","2"]:
            print("请输入正确的选择！")
        elif choice_str == "0":
            print("游戏结束")
            break
        elif choice_str == "1":
            z.main()
        else:
            n.main()
if __name__ == '__main__':
    main()