
# 单生产者单消费者模型
import threading
import queue
N=10
que = queue.Queue(maxsize=N)
semMutex = threading.Semaphore(1)
semEmpty = threading.Semaphore(N)
semFull = threading.Semaphore(0)
Data=1

def producer():
    while(True):
        semEmpty.acquire()
        semMutex.acquire()
        global Data
        Data=Data+1
        que.put(Data)
        print("producer put:",Data)
        semMutex.release()
        semFull.release()

def consumer():
    while(True):
        global Data
        semFull.acquire()
        semMutex.acquire()
        print("consumer get:",que.get())
        semMutex.release()
        semEmpty.release()

if __name__ == '__main__':
    print("程序开始！")
    print("N=",N)
    print("semEmpty._value=",semEmpty._value) 
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("程序结束！")
