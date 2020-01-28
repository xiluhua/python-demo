'''
可变不可变类型
- 不可变类型
    float, int, None, bool, tuple, str, function
- 可变类型
    list, dict, set
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline
print("== function 可变不可变类型 ==")
print("不可变类型")
def add(num):
    num = num+10
    print("num1:", num)

num = 10
add(10)    
print("num2:", num)

pline()

print("可变类型")
def append(num):
    num.append(20)
    print("num3:", num)

num = [10]
append(num)    
print("num4:", num)