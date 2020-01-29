'''
解决参数在一个线程中各个函数之间互相传递的问题
@author: xilh
@since: 20200130
'''
from threading import Thread, current_thread
import threading

# 创建对象
threadLocal = threading.local()

def f1(name):
    print("f1...")
    threadLocal.name = name
    f2()

def f2():
    print("f2...")
    name = threadLocal.name
    print(current_thread().name,", name:", name)

if __name__ == '__main__':
    t1 = Thread(target=f1, name='t1', args=['张三'])
    t2 = Thread(target=f1, name='t2', args=['李四'])
    t1.start()    
    t2.start()    
