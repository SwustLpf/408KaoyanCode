# 408统考2017年第46题

# 题意：某进程中有了个并发执行的线程 threadl、thread2 和thread3，其伪代码如下所示:

'''
//复数的结构类型定义
typedef struct
{
    float a;
    float b;
} cnum;
cnum x, y, z; //全局变量

// 计算两个复数之和
cnum add(cnum p, cnum q)
{
    cnum s;
    s.a = p.a + q.a;
    s.b = p.b + q.b;
    return s;
}

thread1
{
    cnum w;
    w = add(x, y);
}

thread2
{
    cnum w;
    w = add(y, z);
}

thread3
{
    cnum w;
    w.a = 1;
    w.b = 1;
    z = add(z, w);
    y = add(y, w);
}

'''

# 请添加必要的信号量和P、V(或 wa ito 、signa 10〉操作，要求确保线程互斥访问临界资源，并且最大限度地并发执行。


import threading
from time import sleep


class cnum():
    a=0
    b=0

x=cnum()
y=cnum()
z=cnum()
def add(p,q):
    w=cnum()
    w.a=p.a+q.a
    w.b=p.b+q.b
    return w

def thread1():
    global x    
    global y    
    w=cnum()
    w = add(x, y)
    print("thread1, w=(",w.a,",",w.b,")")

def thread2():
    global y    
    global z
    w=cnum()
    w = add(y, z)
    print("thread2, w=(",w.a,",",w.b,")")


def thread3():
    global y    
    global z
    w=cnum()
    w.a = 1
    w.b = 1
    z = add(z, w)
    y = add(y, w)


if __name__ == '__main__':
    print("程序开始！")

    x.a=1
    x.b=2
    y.a=3
    y.b=4
    z.a=5
    z.b=6

    print("before:")
    print("x=(",x.a,",",x.b,")")
    print("y=(",y.a,",",y.b,")")
    print("z=(",z.a,",",z.b,")")

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t3 = threading.Thread(target=thread3)
    sleep(1)
    t3.start()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.join()

    print("after:")
    print("x=(",x.a,",",x.b,")")
    print("y=(",y.a,",",y.b,")")
    print("z=(",z.a,",",z.b,")")
    print("程序结束！")


