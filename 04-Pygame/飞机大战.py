#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:00
# @Author  : Yebiyun
# @Site    : 
# @File    : 飞机大战.py
# @Software: PyCharm



import pygame
from pygame.locals import *
from sys import exit
from random import randint

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

hero_is_hit = False
ticks = 0
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}
# 定义画面帧率
FRAME_RATE = 60

# 定义动画周期（帧数）
ANIMATE_CYCLE = 30

pos = [200, 500]

#英雄类
class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_surface, hero_init_pos):
        super(Hero, self).__init__()
        self.image = hero_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = hero_init_pos

        self.speed = 6
        self.down_index = 0
        self.bullet_sprite = pygame.sprite.Group()

    def move(self, offset):
        x = self.rect[0] + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
        y = self.rect[1] + offset[pygame.K_DOWN] - offset[pygame.K_UP]
        if x < 0:
            self.rect[0] = 0
        elif x > SCREEN_WIDTH - self.rect.width:
            self.rect[0] = SCREEN_WIDTH - self.rect.width
        else:
            self.rect[0] = x

        if y < 0:
            self.rect[1] = 0
        elif y > SCREEN_HEIGHT - self.rect.height:
            self.rect[1] = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect[1] = y

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_surface, bullet_init_pos):
        super().__init__()
        self.image = bullet_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_init_pos

        self.speed = 8

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()

# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_surface, enemy_init_pos):
        super().__init__()
        self.image = enemy_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_init_pos

        self.speed = 2
        self.down_index = 0


    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# 开始
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("飞机大战")

background = pygame.image.load("images/background.gif")

hero_surface = pygame.image.load("images/hero.gif")
hero_down_surface = []
hero_down_surface.append(pygame.image.load("images/hero1.gif"))
hero_down_surface.append(pygame.image.load("images/hero2.gif"))
hero_down_surface.append(pygame.image.load("images/hero3.gif"))
hero_down_surface.append(pygame.image.load("images/hero4.gif"))

bullet_surface = pygame.image.load("images/bullet.gif")

enemy_surface = pygame.image.load("images/smallplane.gif")
enemy_down_surface = []
enemy_down_surface.append(pygame.image.load("images/smallplane1.gif"))
enemy_down_surface.append(pygame.image.load("images/smallplane2.gif"))
enemy_down_surface.append(pygame.image.load("images/smallplane3.gif"))
enemy_down_surface.append(pygame.image.load("images/smallplane4.gif"))

gameover = pygame.image.load("images/gameover.gif")
hero = Hero(hero_surface, pos)
enemy_sprite = pygame.sprite.Group()
# 敌机击毁组
enemy_down_group = pygame.sprite.Group()
clock = pygame.time.Clock()
print(len(hero_down_surface))
while True:
    clock.tick(FRAME_RATE)

    screen.blit(background,(0,0))


    screen.blit(hero.image, hero.rect)
    if ticks % 10 == 0:
        hero.bullet_sprite.add(Bullet(bullet_surface, hero.rect.midtop))

    hero.bullet_sprite.update()
    hero.bullet_sprite.draw(screen)

    if ticks % ANIMATE_CYCLE == 0:
        enemy_sprite.add(Enemy(enemy_surface, (randint(0,SCREEN_WIDTH-enemy_surface.get_width()), -enemy_surface.get_height())))
    enemy_sprite.update()
    enemy_sprite.draw(screen)

    enemy_down_group.add(pygame.sprite.groupcollide(enemy_sprite, hero.bullet_sprite, True, True))
    for enemy in enemy_down_group:
        if ticks % (ANIMATE_CYCLE//2) != 0:
            screen.blit(enemy_down_surface[enemy.down_index], enemy.rect)
        else:
            if enemy.down_index < 3:
                enemy.down_index += 1
            else:
                enemy_down_group.remove(enemy)

    enemy_list = pygame.sprite.spritecollide(hero, enemy_sprite, True)
    if len(enemy_list):
        hero_is_hit = True
        enemy_down_group.add(enemy_list)
    if hero_is_hit:
        if ticks % (ANIMATE_CYCLE//2) != 0:
            hero.image = hero_down_surface[hero.down_index]
        else:
            if hero.down_index < 3:
                hero.down_index += 1
            else:
                break

    pygame.display.update()



    ticks += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = hero.speed

        if event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0

    hero.move(offset)

screen.blit(gameover,(0,0))
ticks = 0
while True:
    clock.tick(FRAME_RATE)
    ticks += 1
    pygame.display.update()
    if ticks % (5*ANIMATE_CYCLE) == 0:
        break


