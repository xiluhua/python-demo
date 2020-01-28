'''
@author: xilh
@since: 20200127
'''

class Father:
    def f1(self):
        print("Father.f1 ...")

class Son(Father):
    def f2(self):
        print("Son.f2 ...")

print("== 单继承 ==")
son = Son()
print(son.f2())    
print(son.f1())    