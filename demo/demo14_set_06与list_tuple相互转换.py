'''
@author: xilh
@since: 20200126
'''
print("== set list tuple 相互转换 ==")
list1 = [i for i in range(10)] + [i for i in range(10)]
print("list1        :", list1)

set1  = set(list1)
print("list to set  :", set1)
tup1  = tuple(list1)
print("list to tuple:", tup1)

list1  = list(set1)
print("set to list  :", list1)
tup1   = tuple(set1)
print("set to tuple :", tup1)

list1  = list(tup1)
print("tuple to list:", list1)
set1   = set(tup1)
print("tuple to set :", set1)