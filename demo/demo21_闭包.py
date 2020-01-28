'''
闭包语法
    - 在函数内部定义了一个新的函数, 并且内部函数引用了外部函数的局部变量, 外部函数将内部函数返回
@author: xilh
@since: 20200127
'''
def outer(num1):
    print("1...")
    def inner(num2):
        print("2...")
        return num1+num2
    return inner

ret = outer(10)
print(ret(100))