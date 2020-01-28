'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline
class Student:
    # 对象被删除时调用
    def __del__(self):
        print("del ...")
        
    def eat(self):
        print("eat ...")
    
    def gotoClass(self):
        print("go to class ...")

# 创建对象
s1 = Student()
s1.eat()
s1.gotoClass()  
pline()
del s1

