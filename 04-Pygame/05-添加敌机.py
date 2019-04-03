# 增加子弹类
import pygame  # 导入pygame库
from pygame.locals import *  # 导入pygame库中的一些常量
from sys import exit  # 导入sys库中的exit函数
from random import randint


# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_surface, enemy_init_pos):
        super(Enemy, self).__init__()
        self.image = enemy_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_init_pos
        self.speed = 2

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_surface, bullet_init_pos):
        super().__init__()
        self.image = bullet_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_init_pos
        self.speed = 8

    # 控制子弹移动
    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()


# 玩家类
class Hero(pygame.sprite.Sprite):

    def __init__(self, hero_surface, hero_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = hero_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = hero_init_pos
        self.speed = 6

        self.bullets1 = pygame.sprite.Group()

    # 控制射击行为
    def single_shoot(self, bullet1_surface):
        bullet1 = Bullet(bullet1_surface, self.rect.midtop)
        self.bullets1.add(bullet1)

    def move(self, offset):
        x = self.rect.left + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
        y = self.rect.top + offset[pygame.K_DOWN] - offset[pygame.K_UP]
        if x < 0:
            self.rect.left = 0
        elif x > SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left = x

        if y < 0:
            self.rect.top = 0
        elif y > SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top = y


# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# 定义画面帧率
FRAME_RATE = 60

# 定义动画周期（帧数）
ANIMATE_CYCLE = 30

ticks = 0
clock = pygame.time.Clock()
offset = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}

# 初始化游戏
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 初始化窗口
pygame.display.set_caption('This is my first pygame-program')  # 设置窗口标题

# 载入背景图
background = pygame.image.load('images/background.gif')

# 载入飞机图片
shoot_img = pygame.image.load('images/shoot.jpg')
# 用subsurface剪切读入的图片
hero_surface = []
hero_surface.append(shoot_img.subsurface(pygame.Rect(0, 99, 102, 126)))
hero_surface.append(shoot_img.subsurface(pygame.Rect(165, 360, 102, 126)))
hero_pos = [200, 500]

# bullet1图片
bullet1_surface = pygame.image.load("images/bullet.gif")

# 敌机图片
enemy1_surface = pygame.image.load("images/smallplane.gif")

# 创建玩家
hero = Hero(hero_surface[0], hero_pos)
enemy_group = pygame.sprite.Group()

# 事件循环(main loop)
while True:

    # 控制游戏最大帧率
    clock.tick(FRAME_RATE)

    # 绘制背景
    screen.blit(background, (0, 0))

    # 改变飞机图片制造动画
    if ticks >= ANIMATE_CYCLE:
        ticks = 0
    hero.image = hero_surface[ticks // (ANIMATE_CYCLE // 2)]

    # 绘制飞机
    screen.blit(hero.image, hero.rect)

    # 射击
    if ticks % 10 == 0:
        hero.single_shoot(bullet1_surface)
    # 控制子弹
    hero.bullets1.update()
    # 绘制子弹
    hero.bullets1.draw(screen)

    # 产生敌机
    if ticks % 30 == 0:
        # get_width()是获取图片的宽度
        enemy = Enemy(enemy1_surface,
                      [randint(0, SCREEN_WIDTH - enemy1_surface.get_width()), -enemy1_surface.get_height()])
        enemy_group.add(enemy)
    # 控制敌机
    enemy_group.update()
    # 绘制敌机
    enemy_group.draw(screen)

    ticks += 1  # python已略去自增运算符

    # 更新屏幕
    pygame.display.update()

    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # ※ Python中没有switch-case 多用字典类型替代
        # 控制方向
        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = hero.speed
        elif event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0

    # 移动飞机
    hero.move(offset)