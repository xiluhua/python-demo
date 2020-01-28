'''
@author: xilh
@since: 20200126
'''
print("== 无序列表交集并集差集==")
set1 = {'a', 'b', 'c'}
set2 = {'c', 'e', 'f'}

set3 = set1.union(set2)
print("set3 union       : ", set3)
set3 = set1 | set2
print("set3 | set2      : ", set3)
set3 = set1.intersection(set2)
print("set3 intersection: ", set3)
set3 = set1 & set2
print("set3 & set2      : ", set3)
set3 = set1.difference(set2)
print("set3 intersection: ", set3)
set3 = set1 - set2
print("set3 - set2      : ", set3)
