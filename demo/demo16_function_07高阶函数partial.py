'''
@author: xilh
@since: 20200126
'''
import functools
from demo.tools.tool import pline
# 二进制
print(int('110', 2))
print(int('111', 2))
print(int('101010', 2))
print(int('101011', 2))
pline()

int2 = functools.partial(int, base=2)
print(int2('110'))
print(int2('111'))
print(int2('101010'))
print(int2('101011'))