# 408统考2019年43题

# 题意：有n（n≥了）位哲学家围坐在一张圆桌边，每位哲学家交替地就餐和思考。在
# 圆桌中心有m（m≥1）个碗，每两位哲学家之间有一根筷子。每位哲学家必须取到一个碗和两
# 侧的筷子后，才能就餐，进餐完毕，将碗和筷子放回原位，并继续思考。为使尽可能多的哲学
# 家同时就餐，且防止出现死锁现象，请使用信号量的口、V操作[wait()、signal()操作〕 描述上
# 述过程中的互斥与同步，并说明所用信号量及初值的含义。


from platform import release
import threading
from time import sleep

N=5
M=3
semChopsticks=[] # N 个筷子

for i in range(0,N):
    semChopsticks.append(threading.Semaphore(1))

semBowls= threading.Semaphore(M)# M 个碗

semMutex=threading.Semaphore(1)

def Phi(k):
    while(True):

        semMutex.acquire() # 防止拿筷子死锁

        semBowls.acquire() # 拿起碗
        semChopsticks[k].acquire() # 拿起左筷子
        semChopsticks[(k+1)%N].acquire() # 拿起右筷子

        semMutex.release()

        print(k," 开始吃饭")

        semChopsticks[k].release()
        semChopsticks[(k+1)%N].release()
        semBowls.release()

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

