# 关于pygame.display.flip()和pygame.display.update()
# flip()是整体刷新
# update（）局部刷新

import pygame
from pygame.locals import *  # 导入pygame库中的一些敞亮
from sys import exit  # 导入sys库中的exit函数
import time

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# 计数ticks
ticks = 0
offset = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}

# 初始化游戏
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 初始化一个用于显示的窗口
pygame.display.set_caption("This is my first pygame-program")  # 设置矿口标题

# 载入背景
background = pygame.image.load("images/background.gif")

# 载入飞机图片
bigplane = pygame.image.load("images/bigplane.gif")

# # 翟茹小飞机图片
# smallplane = pygame.image.load("images/smallplane.gif")
shoot_img = pygame.image.load("images/shoot.jpg")

# 用subsurface剪切读入的图片
hero1_rect = pygame.Rect(0, 99, 102, 126)
hero2_rect = pygame.Rect(165, 360, 102, 126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)

hero_pos = [200, 500]

# 事件循环（main loop）
while True:
    # 绘制背景
    screen.blit(background, (0, 0))

    #     # 绘制飞机
    #     if ticks % 50 < 25:
    #         screen.blit(hero1, hero_pos)
    #     else:
    #         screen.blit(hero2, hero_pos)
    #     ticks += 1
    screen.blit(hero1, hero_pos)

    # 更新屏幕
    pygame.display.update()

    # 处理游戏退出
    # 从消息队列中循环取出
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = 3

        elif event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0

    offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
    hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]
    if hero_pos[0] < 0:
        hero_pos[0] = 0
    elif hero_pos[0] >= SCREEN_WIDTH - hero1_rect.width:
        hero_pos[0] = SCREEN_WIDTH - hero1_rect.width
    else:
        hero_pos[0] = hero_pos[0]

    if hero_pos[1] < 0:
        hero_pos[1] = 0
    elif hero_pos[1] > SCREEN_HEIGHT - hero1_rect.height:
        hero_pos[1] = SCREEN_HEIGHT - hero1_rect.height
    else:
        hero_pos[1] = hero_pos[1]
