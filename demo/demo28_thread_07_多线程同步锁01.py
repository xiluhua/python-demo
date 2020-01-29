'''
多线程共享全局变量, 一个线程修改会影响另一个线程
- 加锁之后本案例最终计算结果: 2000000

@author: xilh
@since: 20200130
'''
from multiprocessing import Lock
from threading import Thread, current_thread


num = 0
# 锁
mylock = Lock()

def f1():
    index = 1
    while index <= 1000000:
        if mylock.acquire():
            global num
            num = num+1
            print(num, '...', current_thread().name)
            index = index+1
            mylock.release()
            
def f2():
    index = 1
    while index <= 1000000:
        if mylock.acquire():
            global num
            num = num+1
            print(num, '...', current_thread().name)
            index = index+1
            mylock.release()
    
if __name__ == '__main__':
    t1 = Thread(target=f1, name='t1')    
    t2 = Thread(target=f2, name='t2')
    t1.start()    
    t2.start()    