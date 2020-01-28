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
    
    def __str__(self):
        return self.name+", "+str(id(self))
    
    def eat(self):
        print("eat ...")
    
    def gotoClass(self):
        print("go to class ...")

# 创建对象
s1 = Student('张三')
s1.eat()
s1.gotoClass()  
pline()
# 这里触发调用 __str__
print(s1)      
