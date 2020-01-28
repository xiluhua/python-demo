'''
可变不可变类型
- 不可变类型
    float, int, None, bool, tuple, str, function
- 可变类型
    list, dict, set
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline

list1 = [1, 2, 3]
list2 = list1       # 改变引用
print("== 列表传递 ==")
print("list1: ", list1)
print("list2: ", list2)
print("== 正例 - 可变类型 - 改变引用 ==")
list2.append(8)
print("list1: ", list1)
print("list2: ", list2)

pline()

list1 = [1, 2, 3]
list2 = list1
print("list1: ", list1)
print("list2: ", list2)
print("== 正例 - 可变类型 - 指向一片新的内存 ==")
list1 = [3, 2, 1]   # 指向一片新的内存
print("list1: ", list1)
print("list2: ", list2)

pline()

num1 = 10
num2 = num1
print("num1: ", num1)
print("num2: ", num2)
print("== 反例 - 不可变类型==")
num1 = num1+100
print("num1: ", num1)
print("num2: ", num2)