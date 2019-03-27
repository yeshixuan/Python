import threading
import time


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        #最多等1秒？
        if mutex.acquire(1):
            num += 1
            msg = self.name + " get num to {}".format(num)
            print(msg)

            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0
# mutex = threading.Lock()
mutex = threading.RLock()

def textTh():
    for i in range(8):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    textTh()