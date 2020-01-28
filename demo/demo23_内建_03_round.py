'''
@author: xilh
@since: 20200127
'''
info  = '1+2'
print(info)
print(eval(info))

infos = "{'sid':1, 'name':'张三', 'age':3}"
ret   = eval(infos)
print(type(ret))
print(ret.get('sid'))