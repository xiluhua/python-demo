'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline

print("== tuple & list 相互转换 ==")
print("list 转 tuple")
list1 = ['physics', 'chemistry', 1997, 2000]
tup   = tuple(list1)
print("tup: \n", "\ttype :", str(type(tup))+"\n", "\tvalue: ", tup)

pline()

print("tuple 转 list")
list1 = list(tup)
print("list1: \n", "\ttype :", str(type(list1))+"\n", "\tvalue: ", list1)

pline()

list1 = list("老王")
print("list1: \n", "\ttype :", str(type(list1))+"\n", "\tvalue: ", list1)
tup   = tuple(list1)
print("tup: \n", "\ttype :", str(type(tup))+"\n", "\tvalue: ", tup)