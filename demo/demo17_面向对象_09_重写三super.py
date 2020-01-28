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

class Father3(Father1, Father2):
    def f(self):
        print("Father3.f ...")
        # 写法一(推荐使用这种: 灵活)
        Father1.f(self)
        Father2.f(self)
        # 写法二
        super().f()
        
print("== 重写三 ==")
fa = Father3()
fa.f()    
