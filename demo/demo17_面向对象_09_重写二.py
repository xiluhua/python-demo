'''
@author: xilh
@since: 20200127
'''

class Father1:
    def f(self):
        print("Father1.f ...")
    def run(self):
        print("Father1.run ...")

class Father2(Father1):
    def f2(self):
        print("Father2.f2 ...")
    def run(self):
        print("Father2.run ...")
        
class Father3:
    def f3(self):
        print("Father3.f3 ...")
    def run(self):
        print("Father3.run ...")

class Son(Father2, Father3):
    def f4(self):
        print("Son.f4 ...")

print("== 重写二 ==")
son = Son()
print(son.f())    
print(son.f3())
print(son.run())
# 打印继承结构
print(Son.__mro__)