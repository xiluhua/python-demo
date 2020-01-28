'''
@author: xilh
@since: 20200127
'''

class Father1:
    def f1(self):
        print("Father1.f1 ...")

class Father2:
    def f2(self):
        print("Father2.f2 ...")

class Son(Father1, Father2):
    def f3(self):
        print("Son.f3 ...")

print("== 多继承 ==")
son = Son()
print(son.f1())    
print(son.f2())    
print(son.f3())    