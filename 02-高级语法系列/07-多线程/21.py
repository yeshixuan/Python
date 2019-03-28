from multiprocessing import Process
import os

def info(title):
    print(title)
    # 当前模块或者进程的名称
    print("module name:", __name__)
    #得到父进程id
    print("parent process:", os.getppid())
    #得到本进程id
    print("process id:", os.getpid())


def f(name):
    info("function f")
    print("hello", name)


if __name__ == '__main__':
    # 主进程
    info("main line")
    p = Process(target=f, args=("bob",))
    p.start()
    p.join()