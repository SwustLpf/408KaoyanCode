# 408统考2020年45题

# 题意: 现有5 个操作A、B、C、D 和 E , 操作C 必须在A 和 B 完成后执行，
# 操作E 必须 在C和D完成后执行，请使用信号量的wait(), signal()。
# 操作(P、V 操作)描述上述操作 之间的同步关系，并说明所用信号量及其初值。

import threading

semAC = threading.Semaphore(0)
semBC = threading.Semaphore(0)
semCE = threading.Semaphore(0)
semDE = threading.Semaphore(0)

def A():
    # semAC.release()
    print("A")

def B():
    # semBC.release()
    print("B")

def C():
    # semAC.acquire()
    # semBC.acquire()
    print("C")
    # semCE.release()

def D():
    print("D")
    # semDE.release()

def E():
    # semCE.acquire()
    # semDE.release()
    print("E")

if __name__ == '__main__':
    print("程序开始！")
    a = threading.Thread(target=A)
    b = threading.Thread(target=B)
    c = threading.Thread(target=C)
    d = threading.Thread(target=D)
    e = threading.Thread(target=E)

    # e.start()
    # d.start()
    # c.start()
    # b.start()
    # a.start()

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    print("程序结束！")

