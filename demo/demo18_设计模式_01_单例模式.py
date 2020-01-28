'''
单例模式
@author: xilh
@since: 20200127
'''

class Singleton:
    
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        print("new ...")
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, num):
        self.num = num

s1 = Singleton(10)
s2 = Singleton(110)
print(s1 == s2)
print(s1 is s2)
