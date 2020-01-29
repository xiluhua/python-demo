'''
@author: xilh
@since: 20200127
'''
info  = '1+2'
print(info)
print(eval(info))

stu = "{'sid':1, 'name':'张三', 'age':3}"
ret   = eval(stu)
print(type(ret))
print(ret.get('sid'))