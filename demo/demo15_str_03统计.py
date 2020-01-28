'''
@author: xilh
@since: 20200126
'''
print("== str 统计 ==")
str1  = "123355666";

count = str1.count("3")
print("count: ", count)
count = str1.count("30")
print("count: ", count)

dict1 = {}
for i in str1:
    dict1[i] = str1.count(i)
print(dict1)    