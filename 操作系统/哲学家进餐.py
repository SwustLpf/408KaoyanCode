# 哲学家进餐模型

from platform import release
import threading
from time import sleep

N=5
semChopsticks=[] # N 个筷子
for i in range(0,N):
    semChopsticks.append(threading.Semaphore(1))
semMutex=threading.Semaphore(1)

def Phi(k):
    while(True):

        semMutex.acquire() # 防止拿筷子死锁

        semChopsticks[k].acquire() # 拿起左筷子
        semChopsticks[(k+1)%N].acquire() # 拿起右筷子

        semMutex.release()

        print(k," 开始吃饭")

        semChopsticks[k].release()
        semChopsticks[(k+1)%N].release()

        print(k," 开始思考")
        sleep(1)


if __name__ == '__main__':
    print("N=",N)
    t=[]
    for i in range(0,N):
        print("i=",i)
        t.append(threading.Thread(target=Phi,args=(i,)))

    for i in range(0,N):
        t[i].start()

    for i in range(0,N):
        t[i].join()

