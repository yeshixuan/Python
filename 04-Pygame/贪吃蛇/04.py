# 载入模块
import sys
import pygame
import os

# 设置常数
CELL_SIZE = 20
UP, DOWN, LEFT, RIGHT = ((0, -CELL_SIZE), (0, CELL_SIZE), (-CELL_SIZE, 0), (CELL_SIZE, 0))

# 画面居中的小技巧
os.environ["SDL_VIDEO_CENTERED"] = "1"
# os.environ["SDL_VIDEO_WINDOW_POS"] = "1664,300"

# 游戏的初始化
pygame.init()
pygame.display.set_caption("pysnake")

# Game
game_clock = pygame.time.Clock()
game_speed = 60
game_screen_width , game_screen_height = 640,680
game_screen = pygame.display.set_mode([game_screen_width , game_screen_height])
game_field = game_screen.get_rect() # <rect (0,0,640,480)>
game_running = True
game_playing = True
game_bgcolor = 0, 0, 0
game_linecolor = 33,33,33

# snake
square_color = 33,255,33
square_color2 = 33,192,33
square_color3 = 192,192,33
square_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
square_direction = RIGHT
square_turn = RIGHT
square_speed = 5 # 美妙走几格
square_delay = 1000 / square_speed # 蛇每次运动的间隔
square_time2move = pygame.time.get_ticks() + square_delay
square_body = [pygame.Rect(0, 0, 0, 0)] * 40 # 蛇的身体

# 主循环
while game_running:
    # print(frames)
    # 1 用户控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
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

    # 2 更新数据
    # 2.1 移动蛇
    if pygame.time.get_ticks() >= square_time2move:
        square_time2move = pygame.time.get_ticks() + square_delay
        square_body = [square_rect] + square_body # 增加一节身体
        square_body.pop()# 截取尾部
        square_direction = square_turn
        square_rect = square_rect.move(square_direction)
        # print("%r" % square_body)

    # 2.2 判断是否game over
    if game_playing:
        # 判断撞墙
        if not game_field.contains(square_rect):
            game_playing = False
        # 撞身体
        for cell in square_body:
            if square_rect == cell:
                game_playing = False
        if not game_playing:
            print("GAME OVER !!!!")


    # 3 更新画面
    if game_playing:
        output = "坐标:%r 速度:%r 范围:%r FPS:%0.2f 时间:%r"
        print(output % (square_rect,square_direction,
                        game_field.contains(square_rect),game_clock.get_fps(),
                        pygame.time.get_ticks()))

        # 3.1 清除屏幕内容
        game_screen.fill(game_bgcolor)
        # 3.2 画格子
        for i in range(CELL_SIZE, game_screen_width, CELL_SIZE):
            pygame.draw.line(game_screen, game_linecolor,
                             (i, 0), (i, game_screen_height))
        for i in range(CELL_SIZE, game_screen_height, CELL_SIZE):
            pygame.draw.line(game_screen, game_linecolor,
                             (0, i), (game_screen_width, i))
        # 3.3 画蛇
        # 画身体
        for cell in square_body:
            game_screen.fill(square_color, cell)
            game_screen.fill(square_color2, cell.inflate(-4, -4))
        # 画头
        game_screen.fill(square_color, square_rect)
        game_screen.fill(square_color3, square_rect.inflate(-4,-4))

    # 3.4 更新窗口内容
    # pygame.display.flip()
    pygame.display.update()
    game_clock.tick(game_speed)

# 退出游戏
pygame.quit()
sys.exit(0)