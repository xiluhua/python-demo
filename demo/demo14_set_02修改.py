'''
@author: xilh
@since: 20200126
'''
print("== 无序列表修改 ==")
set1 = {'a', 'b', 'c'}
print("set1       : ", set1)
set1.add(1)
print("set1 add   : ", set1)

set2 = {'computer', 'calulator'}
set1.update(set2)
print("set1 update: ", set1)
