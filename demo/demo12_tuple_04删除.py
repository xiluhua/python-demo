'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import log

print("== 删除元组 ==")
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000)
print("tup: ", tup)
try:
    del tup
    print ("del tup : ", tup)
except Exception as ex:
    log(4, ex)

