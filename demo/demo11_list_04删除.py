'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline

list1 = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-1 ==")
print("list1      : ", list1)
del(list1[3])
print("del index 3: ", list1)

pline()

list1 = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-2 ==")
print("list1      : ", list1)
list1.pop(3)
print("pop index 3: ", list1)

pline()

list1 = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-3 ==")
print("list1: ", list1)
list1.pop()
print("pop 4: ", list1)

pline()

list1 = ['physics', 'chemistry', 1, 2 ]
print("== 删除列表元素-4 ==")
print("list1         :", list1)
list1.remove(1)
print("remove value 1:", list1)
