'''
@author: xilh
@since: 20200126
'''
print("== 无序列表创建 ==")
set1 = set()
set1.add(123)
print("set1: ", set1)
# 自动去重
set1 = {'a', 'Zara', 'n', 'Class', 'First', 'a', 'b', 'c', 1, 2, 5 ,3, 5, 6}
print("set1: ", set1)

ls   = {"name": '张三', 'age': 30}
set1 = set(ls)
print("set1: ", set1)

tup   = ('张三', '李四')
set1 = set(tup)
print("set1: ", set1)

sdict = {'a': 1, 'b': 2, 'b': ['boy', 'girl', 'children'], 'c': 3 }
set1 = set(sdict)
print("set1: ", set1)
