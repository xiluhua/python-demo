'''
多态:
    - 一个对象不同场景下, 有不同的形态
好处:
    - 开闭原则. 对修改关闭, 对扩展开放
    - 增加可扩展性
@author: xilh
@since: 20200127
'''
from demo.tools.tool import pline

class Animal:
    def run(self):
        pass
    
class Dog(Animal):
    def run(self):
        print("Dog.run ...")
    def eat(self):
        print("Dog.eat ...")
    
class Cat(Animal):
    def run(self):
        print("Cat.run ...")
    def eat(self):
        print("Cat.eat ...")

        
print("== 多态 ==")
dog = Dog()
dog.run()

cat = Cat()
cat.run()
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(dog, object))
print(isinstance(cat, object))

pline()
# 多态应用场景
def run(animal):
    # 强类型校验
    if isinstance(animal, Animal):
        animal.run()
        
def eat(animal):
    animal.eat()

run(dog)    
run(cat)    
eat(dog)    
eat(cat)    