'''
@author: xilh
@since: 20200126
'''
import sys
import traceback
from demo.tools.tool import log

print("== 无序列表删除==")
set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
print("set1            : ", set1)
# discard & remove 区别:
# - 遇到空值: 
#     discard 不报错
#     remove 报错
set1.discard('b')
set1.discard('xxxx')    # 不报错
print("set1 remove('a'): ", set1)
set1.remove('a')
print("set1 remove('a'): ", set1)

try:
    set1.remove('z')    # 报错
except Exception:
    log(4, sys._getframe().f_lineno, traceback.format_exc())

set1.pop()
print("set1 pop        : ", set1)
set1.clear()
print("set1 clear      : ", set1)

