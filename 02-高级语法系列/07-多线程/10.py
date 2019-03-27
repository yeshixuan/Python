import threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        '''
        :param nloop: loop函数的名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print("Start loop", nloop, "at", ctime())
        sleep(nsec)
        print("Done loop", nloop, "at", ctime())


def main():
    print("Starting at:", ctime())

    # ThreadFunc("loop").loop跟以下两个式子相等：
    # t = ThreadFunc("loop")
    # t.loop()

    # 以下t1和t2的定义方式相等
    t = ThreadFunc("loop")
    t1 = threading.Thread(target=t.loop, args=("LOOP1", 4))
    # 下面这种写法更西方人，工业化一点
    t2 = threading.Thread(target=ThreadFunc("loop").loop, args=("LOOP2", 2))

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

    print("All done at:", ctime())


if __name__ == '__main__':
    main()