'''
@author: xilh
@since: 20200129
'''
from _datetime import datetime
import json

from demo.tools.tool import pline, toDict

class Student:
    def __init__(self):
        pass
    
    def init(self, name, age, birth):
        self.name = name
        self.age = age
        self.birth = birth
        
    @classmethod
    def columns(cls):
        print(str(cls))
        return set('name age birth'.split())
    
if __name__ == '__main__':
    
    stu = Student()
    stu.init('张三', 30, datetime.now())
    
    # serialize
    ret1 = json.dumps(stu, default=toDict)
    print('ret1      :', ret1)
    print('type(ret1):', type(ret1))
    pline()
      
    # deserialize
    ret2 = json.loads(ret1)
    print('ret2      :', ret2)
    print('type(ret2):', type(ret2))
    pline()

    # 将字典转化为对象
    stu  = Student()
    stu.__dict__ = ret2;
    # 打印重建的对象
    print("stu       :", type(stu))
    print("stu.age   :", stu.age)
    print("stu.birth :", stu.birth)
    print("stu.birth :", type(stu.birth))