'''
利用time函数，生成量函数
顺序调用
计算总的运行时间
练习带参数的多线程启动方法
'''
import time
import _thread as thread

def loop1(in1):
    # ctime得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    print("我是参数：", in1)
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2(in1, in2):
    print("Start loop 2 at:", time.ctime())
    print("我是参数：", in1, "和参数：", in2)
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())

    thread.start_new_thread(loop1, ("王老大",))
    thread.start_new_thread(loop2, ("王大鹏", "王晓鹏"))

    print("Ending at:", time.ctime())


if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    # while True:
    #     time.sleep(1)
    time.sleep(10)
