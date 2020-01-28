'''
@author: xilh
@since: 20200126
'''
print("== 字典其他功能==")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict2 = sdict.copy()
print("sdict: ", sdict)
print("dict2: ", dict2)
print("dict2 is sdict: ", dict2 is sdict)
print("dict2 == sdict: ", dict2 == sdict)

val   = "abca"  # 键重复会覆盖, 保持唯一
dict2 = dict.fromkeys(val) 
print("dict.fromkeys-1, dict2: ", dict2)
val   = [1, 2, 3]
dict2 = dict.fromkeys(val, 0)
print("dict.fromkeys-2, dict2: ", dict2)

dict3 = {8:'xbox', 9:'xiaobawang'}
dict2.update(dict3)
print("update: ", dict2)