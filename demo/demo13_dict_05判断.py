'''
@author: xilh
@since: 20200126
'''
print("== 字典判断 ==")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("sdict: ", sdict)
print("判断键")
print('Age' in sdict)
print('Age' not in sdict)
print("判断值")
print(7 in sdict.values())
print(7 not in sdict.values())

