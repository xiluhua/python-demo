'''
@author: xilh
@since: 20200126
'''
print("== str 分割 ==")
str1  = "a-b-c";
split = str1.split("-")
print("split -       :", split)

split = str1.split("-", 1)
print("split - 1 time:", split)

split = str1.split(";")
print("split ;       :", split)

str1  = "a b c    d";
split = str1.split()
print("split         :", split)

str1  = "a\nb\tc\n\rp\r    d";
split = str1.split()
print("split         :", split)

str1  = "a-b-c";
partition = str1.partition("-")
print("partition     :", partition)