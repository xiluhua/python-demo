'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline
from demo.tools.tool import rm


# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
sdict = {'a': 1, 'b': 2, 'b': ['boy', 'girl', 'children'], 'c': 3 }
print("sdict: ", sdict)

pline()
# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
sdict = {'a': 1, 'b': 2, 'b': '3'}
print("sdict['b']: ", sdict['b'])
print("sdict     : ", sdict)

pline()

print("修改字典")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
try:
    print("sdict['Age']   : ", sdict['Age'])
    # 如果用字典里没有的键访问数据，会输出错误
    print("sdict['School']: ", sdict['School'])
except Exception as ex:
    print("ERROR: ", ex)    
sdict['Age'] = 8 
print("更新, sdict['Age']   : ", sdict)
sdict['School'] = "RUNOOB"
print("添加, sdict['School']: ", sdict)

pline()

sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("删除字典元素")
print("sdict0: ", sdict)
del sdict['Name']
print("删除键Name, sdict1: ", sdict)
sdict.pop('Age')
print("删除键Age,  sdict2: ", sdict)
sdict.clear()      
print("清空所有字典, sdict3: ", sdict)
sdict = rm(sdict)

if sdict is None:
    print("删除字典, sdict is None ") 

