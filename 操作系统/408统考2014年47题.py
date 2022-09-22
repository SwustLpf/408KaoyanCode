
# 408统考2014年第47题

# 题意：系统中有多个生产者进程和多个消费者进程，共享一个能存放 1000 件产品的环形缓冲 区(初始为空)。 
# 当缓冲区未满时，生产者进程可以放入其生产的一件产品，否则等待;当缓冲 区未空时，消费者进程可以从缓冲区取走一件产品，否则等待。 
# 要求一个消费者进程从缓冲区 连续取出 10 件产品后，其他消费者进程才可以取产品。
# 请使用信号量 P, V C或 wait(), signal()) 操作实现进程间的互斥与同步， 要求写出完整的过程， 并说明所用信号量的含义和初值。


import threading
import queue
N=3
que = queue.Queue(maxsize=N)
semMutex = threading.Semaphore(1)
semEmpty = threading.Semaphore(N)
semOdd = threading.Semaphore(0)
semEven = threading.Semaphore(0)
Data=1

# def producer():
#     while(True):
#         semEmpty.acquire()
#         global Data
#         Data=Data+1

#         semMutex.acquire()
#         que.put(Data)
#         semMutex.release()

#         if(Data % 2==0):
#             print("producerEven put:",Data)
#             semOdd.release()
#         else:
#             print("producerOdd put:",Data)
#             semEven.release()


# def consumerOdd():
#     while(True):
#         semOdd.acquire()

#         semMutex.acquire()
#         Tmp=0
#         queSize=que.qsize()
#         for i in range(0,queSize):
#             Tmp=que.get()
#             if(Tmp%2==0):
#                 que.put(Tmp) # 如果取的不是奇数, 就放回去重新再去
#                 # print(Tmp,"不是奇数")
#             else:
#                 print("consumerOdd get:",Tmp)
#                 break
#         semMutex.release()

#         if(Tmp%2==0):
#             semOdd.release() # 如果缓存中没有奇数, 此次取失败了, 信号量加回去
#         else:
#             semEmpty.release()


# def consumerEven():
#     while(True):
#         semEven.acquire()

#         semMutex.acquire()
#         Tmp=1
#         queSize=que.qsize()
#         for i in range(0,queSize):
#             Tmp=que.get()
#             if(Tmp%2==1):
#                 que.put(Tmp) # 如果取的不是偶数, 就放回去重新再取
#                 # print(Tmp,"不是偶数")

#             else:
#                 print("consumerEven get:",Tmp)
#                 break
#         semMutex.release()

#         if(Tmp%2==1):
#             semEven.release() # 如果缓存中没有偶数, 此次取失败了, 信号量加回去
#         else:
#             semEmpty.release()

# if __name__ == '__main__':
#     print("程序开始！")
#     print("N=",N)
#     print("semEmpty._value=",semEmpty._value) 
#     t1 = threading.Thread(target=producer)
#     t2 = threading.Thread(target=consumerOdd)
#     t3 = threading.Thread(target=consumerEven)
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     print("程序结束！")


