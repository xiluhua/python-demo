'''
公有:
    在类的内外部都可以访问
私有:
    在类的内部访问
@author: xilh
@since: 20200127
'''
from demo.tools.tool import pline

class Student:
    def __init__(self, name):
        print("__init__")
        # 公有
        self.name = name
        pass
    # 私有
    def setAge(self,age):
        self.__age = age
        
    # 私有
    def getAge(self):
        return self.__age
        
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
s1.setAge(30)     
print(s1) 
pline()
print("age:", s1.getAge())

# 报错
print(s1.age)
