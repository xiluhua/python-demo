'''
方法:
    1. 实例方法
        - 使用实例对象访问, 默认使用参数 self, 自动赋值
    2. 类方法
        - 使用类对象访问, 默认使用参数 cls, 自动赋值
    3. 静态方法
        - 实例对象 & 类对象都可以访问. 可以有参, 也可以无参
        
@author: xilh
@since: 20200127
'''
from demo.tools.tool import pline

class Dog:
    name = ''
    age  = 0
    # 实例id(内存地址)
    def showSelfId(self):
        print("id:", id(self))
    
    # 类id(内存地址)
    @classmethod
    def showClsId(cls):
        return id(cls)
        
    @classmethod
    def setName(cls, name):
        print("cls id:", id(cls))
        cls.name=name
    
    @staticmethod
    def run():
        print("run ...")
        
    @staticmethod
    def howl(words):
        print("howl:", words)
     
dog1 = Dog()
print("dog1.name:", dog1.name)
print("dog1.age:", dog1.age)
dog1.showSelfId()

dog2 = Dog()
print("dog2.name:", dog2.name)
print("dog2.age:", dog2.age)
dog2.showSelfId()
pline()

# 添加实例属性, 只有该实例本身可以使用
dog1.gender = 1 
print("dog1.gender: ", dog1.gender)
# 报错
# print("dog2.gender: ", dog2.gender)
pline()

# 添加类属性, 所有实例对象都可以访问
Dog.color = 'white'
print("dog1.color: ", dog1.color)
print("dog2.color: ", dog2.color)
print()

Dog.setName("旺财")
print("Dog.name :", Dog.name)
print("dog1.name:", dog1.name)
print("dog2.name:", dog2.name)
print("dog1.showCls():", dog1.showClsId())
print("dog2.showCls():", dog2.showClsId())
pline()
dog1.howl('dog1: 旺旺旺!')
dog2.howl('dog2: 旺旺!')
Dog.howl('Dog : 旺!')
