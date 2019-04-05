import pygame
import random
from settings import *
from mygame import MyGame
from snake import Snake
from cell import Cell
from field import Field
from apple import Apple

class PySnake(MyGame):
    "贪吃蛇游戏"

    def __init__(self):
        super(PySnake, self).__init__(GAME_NAME, SCREEN_SIZE, FPS,
                                      "resources/Minecraft.ttf", 16, "resources/pysnake.png")
        self.background.fill(BACKGROUND_COLOR)
        for i in range(CELL_SIZE, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.background, GRID_COLOR,
                             (i, 0), (i, SCREEN_HEIGHT))
        for i in range(CELL_SIZE, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.background, GRID_COLOR,
                             (0, i), (SCREEN_WIDTH, i))

        self.field = Field(self, COLUMNS, ROWS)
        self.apple_counter = 0
        self.apple = Apple(self)
        # self.snake = Snake(self)
        self.snake = Snake(self, SNAKE_DEFAULT_X, SNAKE_DEFAULT_Y,
                           SNAKE_DEFAULT_LENGTH, RIGHT, SNAKE_DEFAULT_SPEED,
                           SNAKE_COLOR_SKIN,SNAKE_COLOR_BODY,SNAKE_COLOR_HEAD)

        # 控制按键设定
        self.key_bind(KEY_EXIT, self.quit)
        self.key_bind(KEY_UP, self.snake.turn, direction=UP)
        self.key_bind(KEY_DOWN, self.snake.turn, direction=DOWN)
        self.key_bind(KEY_LEFT, self.snake.turn, direction=LEFT)
        self.key_bind(KEY_RIGHT, self.snake.turn, direction=RIGHT)
        self.key_bind(pygame.K_EQUALS, self.snake.speed_up)
        self.key_bind(pygame.K_MINUS, self.snake.speed_down)
        self.key_bind(KEY_RESPAWN, self.restart)

        self.add_draw_action(self.show_score)

    def restart(self):
        if not self.snake.alive:
            self.apple_counter = 0
            self.field.clear()  # 移除尸体
            self.apple.drop()
            self.snake.respawn()

    def show_score(self):
        text = "Apple {}".format(self.apple_counter)
        output = self.font.render(text, True, (255, 255, 33))
        self.screen.blit(output, (0, 0))

        if not self.snake.alive:
            text = " GAME OVER"
            output = self.font.render(text, True, (255, 33, 33), WHITE)
            self.screen.blit(output, (320 -54 ,240 - 10))
            text = " press R to restart"
            output = self.font.render(text, True, GREY, DARK_GREY)
            self.screen.blit(output, (320 -94 ,260 - 10))

        if not self.running  and self.snake.alive:
            text = " GAME PAUSED"
            output = self.font.render(text, True, LIGTH_GREY, DARK_GREY)
            self.screen.blit(output, (320 -54 ,240 - 10))

if __name__ == '__main__':
    PySnake().run()