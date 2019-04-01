"""

食物
蛇
两者都展示在世界：展示界面， tkinter
使用队列
线程

"""
import random as ra
import queue
import threading
from tkinter import *
import time

class Food():
    def __init__(self, q):
        self.q = q
        self.new_food()
    def new_food(self):
        pos_x = ra.randrange(15, 490, 10)
        pos_y = ra.randrange(25, 290, 10)
        self.pos = pos_x, pos_y
        self.exppos = pos_x - 5, pos_y - 5, pos_x + 5, pos_y + 5
        self.q.put({"food":self.exppos})
        return (pos_x, pos_y)

class Snake(threading.Thread):
    def __init__(self, q, world):
        super(Snake, self).__init__()
        self.q = q
        self.point = 0
        self.world = world
        self.snake_points = [(475, 55), (465, 55), (455, 55), (445, 55)]
        self.food = Food(q)
        self.direction = "Left"
        self.big = False

        self.start()
    def run(self):
        if self.world.is_game_over:
            self._delete()
        while not self.world.is_game_over:
            self.q.put({"move":self.snake_points})
            time.sleep(0.3)
            self.move()

    def move(self):
        # 新蛇头
        new_snake_point = self.snake_leder()
        if new_snake_point == self.food.pos:
            self.point += 10
            self.q.put({"point": self.point})
            self.food.new_food()
            self.big = True
        else:
            if not self.big:
                self.snake_points.pop(0)
            self.big = False
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)
    def check_game_over(self, new_snake_point):
        x, y = new_snake_point
        if (not -5 < x < 505)  or (not -5 < y < 305) or (new_snake_point in self.snake_points):
            self.q.put({"game_over":True})

    def  keypress(self, e):
        self.direction = e.keysym

    def snake_leder(self):
        x, y = self.snake_points[-1]
        if self.direction == "Left":
            x -= 10
        if self.direction == "Right":
            x += 10
        if self.direction == "Up":
            y -= 10
        if self.direction == "Down":
            y += 10
        return (x, y)


class World(Tk):
    def __init__(self, q):
        super(World, self).__init__()
        self.is_game_over = False
        self.q = q
        self.canvas = Canvas(self, width=500, height=300, bg="gray")
        self.canvas.pack()
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="yellow", outline="yellow")
        self.snake = self.canvas.create_line((0, 0), (0, 0), (0, 0), (0, 0), width=10)
        self.score = self.canvas.create_text(460,15,text="score: 0", fill="red")
        self.snake_handler()

    def snake_handler(self):
        try:
            while True:
                # block = False 就算它为空，也不阻塞程序
                task = self.q.get(block=False)
                if task:
                    if task.get("food"):
                        self.canvas.coords(self.food, *task['food'])
                    if task.get("move"):
                        points = [x for point in task["move"] for x in point]
                        # 返回给定项的坐标列表
                        self.canvas.coords(self.snake, *points)
                    if task.get("point"):
                        # 更改它的值
                        self.canvas.itemconfigure(self.score, text="Scored: {}".format(task["point"]))
                    if task.get("game_over"):
                        self.game_over()
                    self.q.task_done()
        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.snake_handler)
    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill="white", text="Game Over!")
        quitBt = Button(self, text="Quit", command=self.myquit)
        againBt = Button(self, text="Again", command=self.again)
        self.canvas.create_window(200, 180, anchor="nw", window=quitBt)
        self.canvas.create_window(200, 210, anchor="nw", window=againBt)
    def myquit(self):
        self.destroy()
    def again(self):
        self.destroy()
        main()

def main():
    q = queue.Queue()
    world = World(q)
    world.title("傻傻的贪吃蛇")
    snake = Snake(q, world)

    world.bind("<Left>", snake.keypress)
    world.bind("<Up>", snake.keypress)
    world.bind("<Right>", snake.keypress)
    world.bind("<Down>", snake.keypress)

    world.mainloop()

if __name__ == '__main__':
    main()