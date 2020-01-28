'''
@author: xilh
@since: 20200126
'''
from demo.tools.tool import pline

print("查询字典")
sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
val   = sdict['Name']
print("1. sdict['Name']    : ", val)

val   = sdict.get('Name')
print("2. sdict.get('Name'): ", val)

pline()    
keys  = sdict.keys() 
print("3. sdict.keys()     : ", keys)
for i in keys:
    print(i)
    
pline()    
vals  = sdict.values() 
print("4. sdict.values()   : ", vals)
for i in vals:
    print(i)

pline()    
items = sdict.items() 
print("4. sdict.items()   : ", items)
for i,j in items:
        print(i, ':', j)