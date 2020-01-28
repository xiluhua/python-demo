'''
@note: https://www.runoob.com/python/python-operators.html
@author: xilh
@since: 20200124
'''

a = 21
b = 10
c = 0

f = 'abc'
g = 'abc'
h = 'efg'

if f == g :
    print("1. f equals g")

if f == h :
    print("2. f equals h")
else :
    print("2. f !equals h")

if a == b :
    print("3. a 等于 b")
else:
    print("3. a 不等于 b")
 
if a != b :
    print("4. a 不等于 b")
else:
    print("4. a 等于 b")
 
if a < b :
    print("5. a 小于 b")
else:
    print("5. a 大于 b")
 
if a > b :
    print("6. a 大于  b")
else:
    print("6. a 小于 b")


# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b :
    print("7. a 小于等于 b")
else:
    print("7. a 大于  b")
 
if b >= a :
    print("8. b 大于等于 a")
else:
    print("8. b 小于 a")

