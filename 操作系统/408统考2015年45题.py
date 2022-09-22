# 408统考2015年第45题

# 题意：有A、B两人通过信箱进行辩论，每个人都从自己的信箱中取得对方的问题。将
# 答案和向对方提出的新问题组成一个邮件放入对方的邮箱中。假设 A 的信箱最多放 M 个邮件，B
# 的信箱最多放 工个邮件。初始时 A 的信箱中有，个邮件（0<x<M，B特箱中有，个(O<y<N
# 辩论者每取出一个邮件，邮件数减 1。A和B两人的操作过程描述如下：

'''
A
{
    while (TRUE) 
    {
        从A的信箱中取出一个邮件
        回答问题并提出一个新问题
        将新邮件放入B的信箱
    }
}

B
{
    while (TRUE) 
    {
        从B的信箱中取出一个邮件
        回答问题并提出一个新问题
        将新邮件放入A的信箱
    }
}
'''

# 当信箱不为空时，辦论者才能从信箱中取邮件，否则需要等待。当信箱不满时，辩论者才
# 能将新邮件放入信箱，否则需要等待。请添加必要的信号量和P、V（或 wait、signal）操作，
# 以实现上述过程的同步。要求写出完整过程，并说明信号量的含义和初值。