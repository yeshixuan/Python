import sys
import pygame
import os

#出现在屏幕正中央
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("pysnake")

game_clock = pygame.time.Clock()
game_speed = 60
game_screen_width , game_screen_height = 640,680
game_screen = pygame.display.set_mode([game_screen_width , game_screen_height])
game_playing = True
game_bgcolor = 33,66,33
square_color = 33,255,33
square_x, square_y = 2, 0
square_size = 20
square_speed_x, square_speed_y  = square_x, 0
square_speed = 2
frames = 0

while game_playing:
    frames += 1
    # print(frames)
    # 用户控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.KEYDOWN:
            # print("键%r, ASCII%r" %(event.unicode, event.key))
            if event.key == pygame.K_UP:
                square_speed_x = 0
                square_speed_y = -square_speed
            elif event.key == pygame.K_DOWN:
                square_speed_x = 0
                square_speed_y = square_speed
            elif event.key == pygame.K_RIGHT:
                square_speed_x = square_speed
                square_speed_y = 0
            elif event.key == pygame.K_LEFT:
                square_speed_x = -square_speed
                square_speed_y = 0

    # 更新数据
    square_x += square_speed_x
    square_y += square_speed_y
    if square_x < 0:
        square_x = 0
    elif square_x > game_screen_width - square_size:
        square_x = game_screen_width - square_size
    if square_y < 0:
        square_y = 0
    elif square_y > game_screen_height - square_size:
        square_y = game_screen_height - square_size
    # 更新画面
    #填充颜色
    game_screen.fill(game_bgcolor)
    #画矩形
    #在0,0的位置上画一个矩形
    pygame.draw.rect(game_screen, square_color,
                     (square_x, square_y, square_size, square_size))
    # pygame.display.flip()
    pygame.display.update()
    #在更新后面为好
    game_clock.tick(game_speed)
pygame.quit()
sys.exit(0)