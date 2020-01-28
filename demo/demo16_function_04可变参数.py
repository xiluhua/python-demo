'''
可变参数: *args
@author: xilh
@since: 20200126
'''
from builtins import type
from demo.tools.tool import pline
print("== 参数-可变参数 ==")
# tuple
def add(*args):
    print(str(type(args)))
    print(args)
    print("sum:", sum(args))

add(10, 20)
pline()
# 不再报错    
add(10)    
pline()
add(10, 20, 30)    
pline()
ls = [100, 200, 300]
add(*ls)
pline()

# dict
def add2(**kwarg):
    print(str(type(kwarg)))
    print(kwarg)

add2(num1=1,num2=2)
num  = {'num1':1, 'num2':2}
add2(**num)   
pline()

# 必须 tuple 在前, dict 在后
def add3(*args, **kwarg):
    print("args type : ", str(type(args)))
    print("kwarg type:", str(type(kwarg)))
    print("args :", args)
    print("kwarg:", kwarg)

add3(*ls, **num)    
