'''
@author: xilh
@since: 20200126
'''
print("== 变量作用域 ==")
# 全局变量
num = 100
def add(num1, num2):
    # 局部变量
    num = num1+num2
    print("num3:", num)

add(10, 20)
print("num :", num)