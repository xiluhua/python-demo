'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline
class Student:
    def __init__(self):
        print("__init__")
        pass
        
    def eat(self):
        print("eat ...")
    
    def gotoClass(self):
        print("go to class ...")

# 创建对象
s1 = Student()
s1.eat()
s1.gotoClass()        
pline()

s2 = Student()
s2.eat()
s2.gotoClass()        
pline()

print(s1 == s2)
print(s1 is s2)
pline()

# 赋值
s1.name  = '张三'
s1.age   = 30
print(s1.name) 
print(s1.age)

# 报错
# print(s2.name) 