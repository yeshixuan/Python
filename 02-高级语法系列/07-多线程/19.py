import multiprocessing
from time import sleep, ctime

def clock(interval):
    while True:
        print("This time is {}.".format(ctime()))
        sleep(interval)


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    #下面两个都行
    # p.join()
    while True:
        print("sleeping>>>>>>>>>>>>>>>")
        sleep(1)