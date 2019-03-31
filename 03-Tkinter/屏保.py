import tkinter
import random
"""
创造球
球进行运动
一旦触及鼠标或者键盘，程序结束
"""

class Create_ball():
    def __init__(self, w, h, csv):
        self.w = w
        self.h = h
        self.csv = csv
        self.step_x = random.randint(5, 20)
        self.step_x = random.choice([self.step_x, -1 * self.step_x])
        self.step_y = random.randint(5, 20)
        self.step_x = random.choice([self.step_y, -1 * self.step_y])

        self.posx = random.randint(10, self.w - 20 )
        self.posy = random.randint(10, self.h - 20)

        c = lambda:random.randint(0,255)
        self.color = "#%02x%02x%02x" % (c(), c(), c())
        self.radius = random.randint(20, 120)
        self.ball_create()
    def ball_create(self):
        x_1 = self.posx - self.radius
        y_1 = self.posy - self.radius
        x_2 = self.posx + self.radius
        y_2 = self.posy + self.radius
        self.ball = self.csv.create_oval(x_1, y_1, x_2, y_2, fill = self.color, outline = self.color)
    def move_ball(self):
        self.posx += self.step_x
        self.posy += self.step_y
        if 0 > self.posx - self.radius:
            self.posx = self.radius
            self.step_x *= -1
        if self.posx + self.radius > self.w:
            self.posx = self.w - self.radius
            self.step_x *= -1
        if 0 > self.posy - self.radius:
            self.posy = self.radius
            self.step_y *= -1
        if self.posy + self.radius > self.h:
            self.posy = self.h - self.radius
            self.step_y *= -1

        self.csv.move(self.ball, self.step_x, self.step_y)

class ScreenRun():
    def __init__(self):

        self.screen = tkinter.Tk()
        #不加1达不到效果
        self.screen.overrideredirect(1)
        self.w, self.h = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
        self.csv = tkinter.Canvas(self.screen, width = self.w, height = self.h)
        self.csv.pack()
        self.balls = self.crt_ball()
        self.screen_run_saver()
        self.csv.bind("<Motion>", self.my_quit)
        self.csv.bind("<Button>", self.my_quit)
        # self.csv.bind("<KeyPress>", self.my_quit)
        self.screen.mainloop()

    def crt_ball(self):
        balls = []
        ball_num = random.randint(6,12)
        for i in range(ball_num):
            ball = Create_ball(self.w, self.h, self.csv)
            balls.append(ball)
        return balls

    def screen_run_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.csv.after(200, self.screen_run_saver)

    def my_quit(self,e):
        self.screen.destroy()
if __name__ == '__main__':
    ScreenRun()
