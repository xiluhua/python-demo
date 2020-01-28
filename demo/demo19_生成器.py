'''
生成器
    - 如果能将列表元素能按一定规则推算出来, 而且可以循环获取这种元素, 
@author: xilh
@since: 20200127
'''
# 遍历 1亿时, 可以发现程序跑的非常慢, 台式机3.4主频, 亲测5-6秒
# import datetime
# ----------------------------------
# from demo.tools.dateTool import DATETIME_FORMAT
# 
# print(datetime.datetime.strftime(datetime.datetime.now(),DATETIME_FORMAT))
# ls = [i for i in range(100000000)]
# print(ls.pop())
# print(datetime.datetime.strftime(datetime.datetime.now(),DATETIME_FORMAT))
# print("over")
# ----------------------------------
from demo.tools.tool import pline

# 生成器主要用在这样的场景
gen = (i for i in range(10))
print(type(gen))
print(next(gen))
print(next(gen))
pline()

for i in gen:
    print(i)
    
#  只能迭代一次， 再迭代就报错
# print(next(gen))
    