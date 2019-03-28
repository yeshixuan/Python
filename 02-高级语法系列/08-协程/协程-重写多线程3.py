# 使用协程的概念，达到一下目的，输入a,b,c,d是个整数，打印出（a+b）*(c+d)的值，假设a+b he c+d是一个耗时1S的IO操作
import asyncio
import threading
import time

async def sum(a, b):
    print("现在开始计算，current thread is {}".format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print("现在计算完了，current thread is {}".format(threading.currentThread()))
    return r

print(time.ctime())
loop = asyncio.get_event_loop()
task = asyncio.gather(sum(1, 2), sum(3, 4))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1 * r2))
loop.close()
print(time.ctime())