'''
@author: xilh
@since: 20200126
'''
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
