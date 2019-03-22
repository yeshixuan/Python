#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 19:07
# @Author  : Yebiyun
# @Site    : 
# @File    : game.py
# @Software: PyCharm
import random as r

class Gui(object):
    def __init__(self):
        self.pow = 100
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        new_x = self.x + r.choice([-1,-2,1,2])
        new_y = self.y + r.choice([-1,-2,1,2])
        if new_x > 10:
            self.x = 10 - (new_x- 10)
        elif new_x < 0:
            self.x = 0 - (new_x)
        else:
            self.x = new_x

        if new_y > 10:
            self.y = 10 - (new_y - 10)
        elif new_y < 0:
            self.y = 0 - new_y
        else:
            self.y = new_y
        self.pow -= 1
        return self.x,self.y

    def eat(self):
        new_pow = self.pow + 20
        if new_pow > 100:
            self.pow = 100
        else:
            self.pow = new_pow


class Fish(object):
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        new_x = self.x + r.choice([-1, 1])
        new_y = self.y + r.choice([-1, 1])
        if new_x > 10:
            self.x = 10 - (new_x - 10)
        elif new_x < 0:
            self.x = 0 - (new_x)
        else:
            self.x = new_x

        if new_y > 10:
            self.y = 10 - (new_y - 10)
        elif new_y < 0:
            self.y = 0 - new_y
        else:
            self.y = new_y
        return self.x, self.y

g = Gui()
fish = []

for i in range(10):
    f = Fish()
    fish.append(f)

while True:
    if not len (fish):
        print("鱼被吃光了，游戏结束！")
        break
    if not g.pow:
        print("乌龟体力耗尽，游戏结束！")
        break
    pos = g.move()
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            print("一条鱼被乌龟吃掉了！")
            g.eat()
            fish.remove(each_fish)


