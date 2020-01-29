'''
线程实现方法：
1. 直接实例化 Thread
2. 继承实现
@author: xilh
@since: 20200130
'''
from threading import current_thread, Thread

def work(num):
    print(num, '子线程 work:', current_thread().name)
    
if __name__ == '__main__':
    print('== 主线程开始 ==')
    # 创建一个线程对象, 指定在运行的时候, 需要完成的任务
    my_thread = Thread(target=work, name='my_thread' ,args=(1, ))
    print(my_thread.name)
    my_thread.start()
    my_thread.join()
    print('== 主进程结束 ==')