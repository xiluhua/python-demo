'''
@author: xilh
@since: 20200126
'''
print("== str 查找 ==")
str1  = "123567590dhgj散热污染123";

index = str1.find("3")
print("exist    :", str(index))
index = str1.find("63")
print("not exist:", str(index))

index = str1.find("3", 10)
print("begin with index 10:", str(index))

# index 没找到会报错, 所以一般使用 find
index = str1.index("3")
print("exist    :", str(index))
index = str1.index("63")
print("not exist:", str(index))