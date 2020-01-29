'''
@author: xilh
@since: 20200128
'''
from _io import StringIO
from demo.tools.tool import pline

# 创建对象
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
ret = f.getvalue()
print(ret)
pline()

f = StringIO("abcdefghijk")
print(f.read(2))
print(f.readline())