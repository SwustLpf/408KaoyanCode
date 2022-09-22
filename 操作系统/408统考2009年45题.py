
# 多生产者多消费者模型

# 408统考2009年第45题

# 题意：三个进程Pr、P2、P，互斥使用一个包含N(N＞0）个单元的缓冲区。P,每次
# 用produceO生成一个正整数并用 putQ送入缓冲区某一空单元中;P,每次用getoddO从该缓冲区
# 中取出一个奇数并用countodd0统计奇数个数;P，每次用 getevenO从该缓冲区中取出一个偶数
# 并用 counteven0统计偶数个数。请用信号量机制实现这三个进程的同步与互斥活动，并说明
# 所定义信号量的含义（要求用伪代码描述）。

import threading
import queue
N=3
que = queue.Queue(maxsize=N)
semMutex = threading.Semaphore(1)
semEmpty = threading.Semaphore(N)
semOdd = threading.Semaphore(0)
semEven = threading.Semaphore(0)
Data=1

def producer():
    while(True):
        semEmpty.acquire()
        global Data
        Data=Data+1

        semMutex.acquire()
        que.put(Data)
        semMutex.release()

        if(Data % 2==0):
            print("producerEven put:",Data)
            semOdd.release()
        else:
            print("producerOdd put:",Data)
            semEven.release()


def consumerOdd():
    while(True):
        semOdd.acquire()

        semMutex.acquire()
        Tmp=0
        queSize=que.qsize()
        for i in range(0,queSize):
            Tmp=que.get()
            if(Tmp%2==0):
                que.put(Tmp) # 如果取的不是奇数, 就放回去重新再去
                # print(Tmp,"不是奇数")
            else:
                print("consumerOdd get:",Tmp)
                break
        semMutex.release()

        if(Tmp%2==0):
            semOdd.release() # 如果缓存中没有奇数, 此次取失败了, 信号量加回去
        else:
            semEmpty.release()


def consumerEven():
    while(True):
        semEven.acquire()

        semMutex.acquire()
        Tmp=1
        queSize=que.qsize()
        for i in range(0,queSize):
            Tmp=que.get()
            if(Tmp%2==1):
                que.put(Tmp) # 如果取的不是偶数, 就放回去重新再取
                # print(Tmp,"不是偶数")

            else:
                print("consumerEven get:",Tmp)
                break
        semMutex.release()

        if(Tmp%2==1):
            semEven.release() # 如果缓存中没有偶数, 此次取失败了, 信号量加回去
        else:
            semEmpty.release()

if __name__ == '__main__':
    print("程序开始！")
    print("N=",N)
    print("semEmpty._value=",semEmpty._value) 
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumerOdd)
    t3 = threading.Thread(target=consumerEven)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("程序结束！")


