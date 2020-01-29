'''
@author: xilh
@since: 20200128
'''
import json

from demo.tools.tool import pline

class Student:
    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age
        
def dict_student(d):
    return Student(d['name'], d['age'])

stu = Student('张三', 30)
    
# serialize
ret1 = json.dumps(stu.__dict__)
print('ret1      :', ret1)
print('type(ret1):', type(ret1))
 
# deserialize
ret2 = json.loads(ret1)
print('ret2      :', ret2)
print('type(ret2):', type(ret2))
pline()

