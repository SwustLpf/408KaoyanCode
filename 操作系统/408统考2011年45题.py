
# 408统考2011年第45题

# 题意：某银行提供1个服务窗口和10个供顾客等待的座位。 顾客到达银行时，
# 若有空 座位，则到取号机上领取一个号，等待叫号。取号机每次仅允许一位顾客使用。 当营业员空闲时，
# 通过叫号选取 一位顾客， 并为其服务。 顾客和营业员的活动过程描述如下:
'''
cobegin
{
    process 顾客i
    {
        从取号机获取一个号码
        等待叫号
        获取服务
    }

    process 菅业员
    { 
        while (TRUE)
        {
            叫号：
            为客户服务；
        }
    }
}
coend
'''

import threading
import queue
from time import sleep
N=10
que = queue.Queue(maxsize=N)
semMutex = threading.Semaphore(1) # 互斥使用取号机
semEmpty = threading.Semaphore(N) # 空座位的数量
semFull = threading.Semaphore(0) # 已占座位的数量
semService = threading.Semaphore(0) # 等待叫号
callNumber=1 # 排队号



def consumer():
    while(True):

        semEmpty.acquire() # 等空位

        semMutex.acquire() # 互斥使用取号机
        global callNumber
        callNumber+=1
        print("从取号机获取一个号码:",callNumber)
        que.put(callNumber)
        semMutex.release() # 互斥使用取号机

        print(callNumber,"等待叫号")
        semFull.release() # 通知营业员有顾客
        semService.acquire() # 等待营业员叫号
        print(callNumber,"获取服务")


def assistant():
    while(True):
        semFull.acquire() # 等有顾客到来
        Tmp=que.get()
        print("为",Tmp,"号服务")
        sleep(1)
        semService.release() # 营业员叫号
        semEmpty.release() # 顾客离开产生新的空位



if __name__ == '__main__':
    print("程序开始！")
    print("N=",N)
    print("semEmpty._value=",semEmpty._value) 
    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=assistant)
    # t3 = threading.Thread(target=consumerEven)
    t1.start()
    t2.start()
    # t3.start()
    t1.join()
    t2.join()
    # t3.join()
    print("程序结束！")


