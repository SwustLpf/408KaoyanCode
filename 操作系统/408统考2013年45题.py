
# 408统考2013年第45题

# 题意：某博物馆最多可容纳 500人同时参观，有一个出入口，该出入口一次仅允许1个人通过。参观者的活动描述如下:
# 请添加必要的信号量和P、V(或 waito、signal0）操作，以实现上达过程中的互斥与同步。
# 要求写出完整的过程，说明信号量的含义并赋初值
'''
cobegin
{
    参观者进程 i:
    {
        进门：
        参观；
        出门：
    }
}
coend
'''

# 这道题挺简单的, 为了有效果，设置进门很快，出门的时间很慢，因此会出现一下子博物馆的人很多的现象

import threading
import queue
from time import sleep
N=500
que = queue.Queue(maxsize=N)
semMutex = threading.Semaphore(1) # 出入口互斥
semEmpty = threading.Semaphore(N) # 空位的数量
Number=0 # 第几个进入的人



def threadRun():
    # while(True):

    semEmpty.acquire() # 等空位

    semMutex.acquire() # 出入口互斥
    global Number
    Number+=1
    # sleep(0.1)
    print("第",Number,"个人进门")
    que.put(Number)
    semMutex.release() # 出口互斥

    sleep(1)
    semMutex.acquire() # 出入口互斥
    Tmp = que.get()
    print("第",Tmp,"个人出门")
    semMutex.release() # 出口互斥

    semEmpty.release()



if __name__ == '__main__':
    print("程序开始！")
    print("N=",N)
    print("semEmpty._value=",semEmpty._value) 

    # t1 = threading.Thread(target=threadRun)
    # t1.start()
    # t1.join()
    N=500
    a=[]
    for i in range(0,N):
        a.append(threading.Thread(target=threadRun))

    # for i in range(0,N):
    #     a[i].start()
    
    # for i in range(0,N):
    #     a[i].join()
    print("程序结束！")


