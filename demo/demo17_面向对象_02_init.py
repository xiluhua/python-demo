'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline
class Student:
    def __init__(self, name):
        print("__init__")
        self.name = name
        pass
        
    def eat(self):
        print("eat ...")
    
    def gotoClass(self):
        print("go to class ...")

# 创建对象
s1 = Student('张三')
s1.eat()
s1.gotoClass()
print(s1)
pline()

# 报错
# s2 = Student()
