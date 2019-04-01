import tkinter

root = tkinter.Tk()
root.resizable(width=False,height=False)

canvas = tkinter.Canvas(root,width =480,height=600)
canvas.pack()


bg_img_name = "../img/background.gif"
bg_img = tkinter.PhotoImage(file=bg_img_name)
canvas.create_image(240,300,anchor=tkinter.CENTER,image=bg_img,tags="bg")

m = 50
n = 50
w = 60
h = 50
nw = [50,50]
ne = [100,50]
bee_img_name = "../img/bee.gif"
bee_img = tkinter.PhotoImage(file=bee_img_name)
canvas.create_image(m,n,anchor=tkinter.NW,image=bee_img,tags="bee")
step = [5,3]
direction = [1,1]

def exec_move():
    global nw
    global ne
    global step
    global direction
    # 左右碰壁时x轴反向
    if nw[0] < 5 or ne[0] > 480 - 5:
        direction[0] *= -1

    if nw[1] <600:
        # Y轴边界之内正常移动
        x = 5 * direction[0]
        y = 3 * direction[1]
        nw[0] += x
        nw[1] += y
        ne[0] += x
        ne[1] += y
        canvas.move("bee", x, y)
    else:
        # 边界之外错误处理
        canvas.move("bee", 0, -600)
        direction[0] = 1
        nw[1] -= 600
        ne[1] -= 600
    canvas.after(50,exec_move)
    root.mainloop()

exec_move()


