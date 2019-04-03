"""
1. 继承Sprite类编写自己的类
2. 建立精灵组
3. 控制精灵组行为
4. 绘制精灵组成员到screen上

两个属性：self.image, self.rect
方法：self.update() 在Sprite类中，update函数是空的,重写这个函数主要是方便当我们把精灵添加到组时，
调用Group.update()会调用全体精灵的update()，这样我们就方便控制全体精灵的行为了
"""

import pygame
from pygame.locals import *
from sys import exit
from random import randint

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


# Player类--继承自pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        #         pygame.sprite.Sprite.__init__(self)    # 父构造函数
        #         super(Player, self).__init__()
        super().__init__()
        self.image = pygame.Surface([10, 10])  # 精灵图片Surface
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()  # 精灵图片的大小
        self.rect.topleft = initial_position  # 精灵图片的位置

        self.speed = 6


    def update(self):
        self.rect.left += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# 建立精灵组
group = pygame.sprite.Group()

while True:
    clock.tick(10)
    print(len(group.sprites()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 绘制背景
    screen.fill((255, 255, 255))

    # 不断网精灵组添加精灵
    group.add(Player((randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))))

    # 将每个精灵更新后显示在Screen上
    group.update()
    group.draw(screen) #把所有精灵画到屏幕上

    pygame.display.update()


