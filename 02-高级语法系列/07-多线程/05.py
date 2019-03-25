#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
# 导入多线程处理包
import threading

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
    # 生成thread.Thread实例
    t = threading.Thread(target=loop1, args=("王老大",))
    t1 = threading.Thread(target=loop2, args=("王大鹏", "王晓鹏"))
    t.start()
    t1.start()
    # 有了join（） 主线程会等待子线程完成后结束
    # 没有join() 主线程不会等子线程，但是不用while，子线程的结尾都会打印出来
    t.join()
    t1.join()

    print("Ending at:", time.ctime())


if __name__ == '__main__':
    main()
    # 不需要while