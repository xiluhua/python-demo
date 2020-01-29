'''
线程的同步:
    - 协同步调, 按照约定的顺序执行
@author: xilh
@since: 20200130
'''
from multiprocessing import Lock
mylock = Lock()
print(mylock)
print('1...')
# 获得锁
mylock.acquire()
print('2...')
# 释放锁, 这一句注解的话, 下面这句没法执行, 没法获得锁
mylock.release()
print('3...')
mylock.acquire()
print('4...')

