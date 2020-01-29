'''
多任务
@author: xilh
@since: 20200130
'''
from multiprocessing import Process
from threading import Thread
import time

from demo.tools.tool import pline


def sing():
    for i in range(3):
        print("正在唱歌...", i)
        time.sleep(0.2)

def dance():
    for i in range(3):
        print("正在跳舞...", i)
        time.sleep(0.2)

def p():
    p1 = Process(target=sing)
    p2 = Process(target=dance)
    p1.start()
    p2.start()

def t():
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()

if __name__ == '__main__':
    # 进程跑
    p()
    
    time.sleep(1)
    pline()
    
    # 线程跑
    t() 