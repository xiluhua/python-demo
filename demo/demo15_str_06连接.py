'''
@author: xilh
@since: 20200126
'''
print("== str 连接 ==")
str1  = "I am ironman";
ls    = str1.split();
print("ls  :", ls)
str2  = ''.join(ls)
print("str2:", str2)
str2  = '/'.join(ls)
print("str2:", str2)
str2  = ' '.join(ls)
print("str2:", str2)
