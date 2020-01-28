'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline
print("== 匿名函数 ==")
f1 = lambda x:x+1
f2 = lambda x:x*x

print(f1(1))
print(f2(2))
print(f2(4))
pline()

ls  = {2,4,6}
val = list(map(lambda x:x*x, ls))
print(val)
pline()

ls2 = {3,5,7}
val = list(map(lambda x,y:x*y, ls, ls2))
print(val)
pline()

