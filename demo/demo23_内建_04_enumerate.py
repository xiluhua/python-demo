'''
@author: xilh
@since: 20200127
'''
from demo.tools.tool import pline
ls = ['a', 'b', 'c', 'd', 'e']
en = enumerate(ls)
print(next(en))
pline()

for i in en:
    print(i)
pline()

en = enumerate(ls, 2)
for i in en:
    print(i)
