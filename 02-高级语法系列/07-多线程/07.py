import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
# 设置守护线程的方法，必须再start之前设置，否则无效
# t1.setDaemon(True)
t1.daemon = True
t1.start()
t1.join()# 如果设置了它，反正主程序会等线程的，所以设不设置守护就没关系

time.sleep(1)
print("Main thread end")