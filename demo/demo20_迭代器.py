'''
迭代器
    - 访问集合元素的一种方式, 可以记住迭代的位置，从第一个到最后一个, 只能迭代一轮
    1. 判断一个对象是否可以迭代  - 用 for 循环都可以跑. 但是不一定是迭代器
    2. 迭代器 - 使用 next 来获取下一个值
    3. 使用迭代器的场景: 在程序需要处理大量集合数据的时候, 减少占用内存
@author: xilh
@since: 20200127
'''
import collections
from demo.tools.tool import pline
ls   = [1,2,3]
print("ls   Iterable:", isinstance(ls, collections.Iterable))
print("ls   Iterator:", isinstance(ls, collections.Iterator))
# 转迭代器
it   = iter(ls)
print("it   Iterator:", isinstance(it, collections.Iterator))
pline()

info = "1234"
print("info Iterable:", isinstance(info, collections.Iterable))
print("info Iterator:", isinstance(info, collections.Iterator))
# 转迭代器
it   = iter(info)
print("it   Iterator:", isinstance(it, collections.Iterator))
pline()

# 本身就是迭代器
ge   = (i for i in range(10))
print("ge   Iterable:", isinstance(ge, collections.Iterable))
print("ge   Iterator:", isinstance(ge, collections.Iterator))
