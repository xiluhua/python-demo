'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import log
print("== 访问列表中的值 ==")
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print("list1[0]  : ", list1[0])
print("list2[1:5]: ", list2[1:5])

print("== 根据列表中的值找下标 ==")
print("index : ", list1.index(1997))
print("count1: ", list1.count(1997))    # 存在
print("count2: ", list1.count(5))       # 不存在
try:
    print("not in: ", list1.index(5))
except Exception as es:
    log(4, es)