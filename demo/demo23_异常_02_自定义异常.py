'''
自定义异常:
    - 继承异常类(Exception)
@author: xilh
@since: 20200127
'''
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg
        pass

age = 30
if age > 10:
    raise MyException('年龄不能大于 10 岁')
