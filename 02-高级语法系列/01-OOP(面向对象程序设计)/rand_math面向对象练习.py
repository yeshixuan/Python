#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 21:34
# @Author  : Yebiyun
# @Site    : 
# @File    : rand_math面向对象练习.py
# @Software: PyCharm

'''
输入一个三位数与程序随机数比较大小
1如果大于程序的随机数，分别输出这个三位数的各位\十位\百位
2如果等于程序随机数，则提示中奖，记100分
3如果小于程序随机数，则将120个字符输入到文本文件中
（规则是每条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字
'''
import random as ra

class Games(object):
    def __init__(self, num, score):
        self.randm = ra.randint(100,999)
        self.num = num
        self.score = score
    def content(self):
        str_num = ""
        str_str = ""
        for i in range(8):
            str_num += str(ra.randint(0,9) )
        for i in range(4):
            num = ra.randint(97, 122)
            s = chr(num)
            str_str += s

        return str_str + str_num
    def bigger(self):
        ge = self.num % 10
        shi = (self.num % 100) // 10
        bai = self.num // 100
        print("您输入的数字的百位数是：%s，十位数是：%s，个位数是：%s。" %(bai, shi, ge))

    def equal(self):
        self.score = self.score + 100
        print("天呐，您太厉害了，这么小概率的事都能猜中，奖励您100分，您目前的积分是{}分！".format(self.score))

    def smaller(self):
        # print("您输入的数字比随机数小哦！")

        for i in range(10):
            str_text = self.content()
            with open("rand_math.text","a") as f:
                f.write(str_text + "\n")
                f.close()
        print("给您写了点东西，您看下吧！")

    def compare(self):
        if self.num > self.randm:
            self.bigger()
        if self.num == self.randm:
            self.equal()
        if self.num < self.randm:
            self.smaller()
def run_game(num, score):
    while True:
        switch = True
        ga = Games(num, score)
        ga.compare()
        while True:
            choice = input("请选择是否继续游戏！1表示继续游戏，0表示结束游戏（0/1）：")
            if not choice.isdigit():
                continue
            if int(choice) not in [0,1]:
                continue
            if int(choice) == 0:
                switch = False
                break
            if int(choice) == 1:
                switch = True
                break
        break
    return switch

def main():
    print("欢迎进入猜数字游戏！")
    score = ra.randint(0,1000)
    print("您的初始游戏分数是：{}".format(score))
    while True:
        num = input("请输入一个三位数：")
        if num.isdigit():
            num = int(num)
            if 100 <= num <= 999:
                switch = run_game(num, score)
                if switch == True:
                    continue
                else:
                    break
            else:
                print("数字必须为三位数！")
        else:
            print("请输入纯数字！")

if __name__ == '__main__':
    main()

