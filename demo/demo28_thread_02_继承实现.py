'''
线程实现方法：
1. 直接实例化 Thread
2. 继承实现
开发中推荐使用第二种, 使用面向对象完成, 利于功能的扩展    
@author: xilh
@since: 20200130
'''
from threading import Thread, current_thread
import time


class MyThread(Thread):
    def __init__(self, pname, a, b):
        # 这句话不能少
        Thread.__init__(self, name = pname)
        self.a = a
        self.b = b
        
    def run(self):
        print(self.name+":",self.a, self.b)
        print("Run Child Thread, name = {}".format(current_thread().name))
        time.sleep(3)
        
if __name__ == '__main__':
    print('主线程开始')
    t1 = MyThread('t1', 1, 2)
    print("t1.name:", t1.name)
    t1.start()
    
    t2 = MyThread('t2', 3, 4)
    print("t2.name:", t2.name)
    t2.start()
    
    t1.join()
    t2.join()
    print('主进程结束')