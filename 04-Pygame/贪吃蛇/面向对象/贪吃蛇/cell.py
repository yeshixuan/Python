
class Cell(object):
    "方块类"

    def __init__(self, x, y, color1, color2):
        self.x = x
        self.y = y
        self.color1, self.color2 = color1, color2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy