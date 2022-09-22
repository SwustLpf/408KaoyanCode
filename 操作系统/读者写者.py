# 读者写者模型

import threading
from time import sleep

semRW = threading.Semaphore(1)
semMutex = threading.Semaphore(1)
readerCount = 0


def writer():
    while(True):
        semRW.acquire()
        print("Writing...")
        semRW.release()
        # sleep(1)


def reader(k):
    while(True):
        global readerCount

        semMutex.acquire()  # 对 readerCount 变量进行保护
        if(0 == readerCount):
            semRW.acquire()
        readerCount += 1
        semMutex.release()

        print("Reading...", k)

        semMutex.acquire()
        readerCount -= 1
        if(0 == readerCount):
            semRW.release()
        semMutex.release()


if __name__ == '__main__':
    print("程序开始！")

    w = threading.Thread(target=writer)
    N = 10

    r = []
    for i in range(0, N):
        r.append(threading.Thread(target=reader, args=(i,)))

    for i in range(0, N):
        r[i].start()
    w.start()

    w.join()
    for i in range(0, N):
        r[i].join()

    print("程序结束！")
