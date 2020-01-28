'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline
print("== 字典遍历==")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

for k in sdict:
    print(k, ": ", sdict.get(k))

pline()

for k, v in sdict.items():
    print(k, ": ", v)

