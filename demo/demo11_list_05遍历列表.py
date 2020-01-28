'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline

list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("== 遍历列表-1 ==")

i = 0
length = len(list2)
while i< length:
    print(list2[i])
    i = i+1
    
pline()
print("== 遍历列表-2 ==")
for i in list2:
    print(i)