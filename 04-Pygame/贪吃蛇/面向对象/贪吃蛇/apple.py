from settings import *
from cell import Cell
from random import randint

class Apple(Cell):
    "单调的食物"

    def __init__(self, game):
        super(Apple, self).__init__(0, 0, APPLE_COLOR1, APPLE_COLOR2)
        self.field = game.field
        self.drop()

    def drop(self):
        while True:
            x, y = randint(0, COLUMNS - 1), randint(0, ROWS - 1)
            if self.field.get_cell(x, y) is None:
                self.x, self.y = x, y
                self.field.put_cell(self)
                break