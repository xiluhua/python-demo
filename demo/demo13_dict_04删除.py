'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import rm

sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("删除字典元素")
print("sdict0: ", sdict)
del sdict['Name']
print("del Name, sdict1: ", sdict)
sdict.pop('Age')
print("pop Age,  sdict2: ", sdict)
sdict.clear()      
print("清空所有字典, sdict3: ", sdict)
sdict = rm(sdict)

if sdict is None:
    print("删除字典, sdict is None ") 

