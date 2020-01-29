'''
@author: xilh
@since: 20200130
'''
import multiprocessing
import os
import time

from demo.tools.tool import pline


def runChildProcess(name, a, b):
    print("Run Child Process, ppid = {}, pid = {}, pname = {}".format(os.getppid(), os.getpid(), name))
    time.sleep(3)
    print('不会打印')
    
if __name__ == '__main__':
    print("Run Parent Process, pid =", os.getpid())
    child = multiprocessing.Process(target=runChildProcess,args=('test', 10, 20))
    pline()
    child.start()
    # 查看进程状态
    print(child.is_alive())
    # 关闭子进程
    child.terminate()
    time.sleep(0.01)
    # 查看进程状态
    print(child.is_alive())
    print('主进程结束')