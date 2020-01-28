'''
@author: xilh
@since: 20200124
'''

a = 20
b = 20
 
if ( a is b ):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")
 
if ( a is not b ):
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
    
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。    
a = [1, 2, 3]
b = a
print(b is a) # True
print(b == a) # True

b = a[:]
print(b is a)
print(b == a)
