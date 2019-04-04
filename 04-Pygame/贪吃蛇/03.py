import sys
import pygame
import os

#出现在屏幕正中央
os.environ["SDL_VIDEO_CENTERED"] = "1"
os.environ["SDL_VIDEO_WINDOW_POS"] = "1664,300"
pygame.init()

pygame.display.set_caption("pysnake")

game_clock = pygame.time.Clock()
game_speed = 60
game_screen_width , game_screen_height = 640,680
game_screen = pygame.display.set_mode([game_screen_width , game_screen_height])
game_field = game_screen.get_rect() # <rect (0,0,640,480)>
game_running = True
game_bgcolor = 0, 0, 0
game_linecolor = 33,33,33
square_color = 33,255,33
square_color2 = 33,192,33

CELL_SIZE = 20
square_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
UP, DOWN, LEFT, RIGHT = ((0, -CELL_SIZE), (0, CELL_SIZE), (-CELL_SIZE, 0), (CELL_SIZE, 0))
square_direction = RIGHT
square_turn = RIGHT
square_speed = 5 # 美妙走几格
square_delay = 1000 / square_speed # 蛇每次运动的间隔
square_time2move = pygame.time.get_ticks() + square_delay

while game_running:
    # print(frames)
    # 用户控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            # print("键%r, ASCII%r" %(event.unicode, event.key))
            if square_direction in [LEFT, RIGHT]:
                if event.key == pygame.K_UP:
                    square_turn = UP
                elif event.key == pygame.K_DOWN:
                    square_turn = DOWN
            if square_direction in [UP, DOWN]:
                if event.key == pygame.K_RIGHT:
                    square_turn = RIGHT
                elif event.key == pygame.K_LEFT:
                    square_turn = LEFT

    # 更新数据
    # if square_rect.x % CELL_SIZE == 0 and square_rect.y % CELL_SIZE == 0:
    if pygame.time.get_ticks() >= square_time2move:
        square_time2move = pygame.time.get_ticks() + square_delay
        square_direction = square_turn
        square_rect = square_rect.move(square_direction)
    output = "坐标:%r 速度:%r 范围:%r FPS:%0.2f 时间:%r"
    print(output % (square_rect,square_direction,
                    game_field.contains(square_rect),game_clock.get_fps(),
                    pygame.time.get_ticks()))
    # 更新画面
    #填充颜色
    game_screen.fill(game_bgcolor)
    for i in range(CELL_SIZE, game_screen_width, CELL_SIZE):
        pygame.draw.line(game_screen, game_linecolor,
                         (i, 0), (i, game_screen_height))
    for i in range(CELL_SIZE, game_screen_height, CELL_SIZE):
        pygame.draw.line(game_screen, game_linecolor,
                         (0, i), (game_screen_width, i))
    game_screen.fill(square_color, square_rect)
    game_screen.fill(square_color2, square_rect.inflate(-4,-4))
    # pygame.display.flip()
    pygame.display.update()
    #在更新后面为好
    game_clock.tick(game_speed)
pygame.quit()
sys.exit(0)