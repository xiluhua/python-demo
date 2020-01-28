'''
@author: xilh
@since: 20200127
'''

class Father:
    def __init__(self, name):
        print("Father.f1 ...")
        self.name = name

class Son(Father):
    def __init__(self, name, age):
        print("Son.f2 ...")
        Father.__init__(self, name)
        self.age = age
        
print("== 重写四, 重写 __init__ ==")
son = Son('张三', 30)
print(son.age, son.name)    