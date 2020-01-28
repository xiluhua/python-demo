'''
@author: xilh
@since: 20200126
'''
print("== 无序列表判断 ==")
set1 = {'a', 'b', 'c'}
set2 = {'a', 'b' }
set3 = {'z', 'v' }

print("set2.issubset(set1)  :", set2.issubset(set1))
print("set1.issuperset(set2):", set1.issuperset(set2))

print("set1.isdisjoint(set2):", set1.isdisjoint(set2))
print("set1.isdisjoint(set3):", set1.isdisjoint(set3))

print("a in set1:", 'a' in set1)
print("x in set1:", 'x' in set1)