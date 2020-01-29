'''
@author: xilh
@since: 20200128
'''
from _io import BytesIO
from demo.tools.tool import pline

# 创建对象
f = BytesIO()
f.write('hello'.encode(encoding='utf_8'))
f.write(' '.encode(encoding='utf_8'))
f.write('world'.encode(encoding='utf_8'))
f.write(' '.encode(encoding='utf_8'))
f.write('张三'.encode(encoding='utf_8'))
# 获取值
ret = f.getvalue()
print(ret)
pline()

f = BytesIO('张三是程序员'.encode('utf-8'))
print(f.readline())
# 关闭
f.close()