'''
@author: xilh
@since: 20200127
'''

class Father1:
    def f(self):
        print("Father1.f ...")

class Father2:
    def f(self):
        print("Father2.f ...")

class Son(Father1, Father2):
    def f3(self):
        print("Son.f3 ...")

print("== 重写一 ==")
son = Son()
print(son.f())    
print(son.f3())
# 打印继承结构
print(Son.__mro__)