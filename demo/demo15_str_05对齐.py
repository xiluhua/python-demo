'''
@author: xilh
@since: 20200126
'''
print("== str 对齐 ==")
str1  = "I am ironman";
str2 = str1.ljust(30)
print("ljust:")
print(str2)

str2 = str1.ljust(30, "*")
print("ljust:")
print(str2)

str2 = str1.ljust(3)
print("ljust:")
print(str2)

str2 = str1.rjust(30)
print("rjust:")
print(str2)

str2 = str1.rjust(30, "*")
print("rjust:")
print(str2)

str2 = str1.center(30)
print("center:")
print(str2)

str2 = str1.center(30, "*")
print("center:")
print(str2)



