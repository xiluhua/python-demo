'''
多线程共享全局变量, 一个线程修改会影响另一个线程
- 本案例最终计算结果应该是 2000000, 但是结果不是!!!

@author: xilh
@since: 20200130
'''
from threading import Thread, current_thread

num = 0

def f1():
    index = 1
    while index <= 1000000:
        global num
        num = num+1
        print(num, '...', current_thread().name)
        index = index+1

def f2():
    index = 1
    while index <= 1000000:
        global num
        num = num+1
        print(num, '...', current_thread().name)
        index = index+1
    
if __name__ == '__main__':
    t1 = Thread(target=f1, name='t1')    
    t2 = Thread(target=f2, name='t2')
    t1.start()    
    t2.start()    