'''
装饰器带参数
@author: xilh
@since: 20200127
'''
def outer(fn):
    print("1...")
    def inner(*args, **kwargs):
        print("2...")
        return fn(*args, **kwargs)
    return inner

@outer
def func1():
    print('func1...')

@outer
def func2():
    print('func2...')
    return '222'

@outer
def func3(a, b):
    print('func3...')

def func4(a, b):
    print('func4...')
    return '444'

func1()
# 有参数
func3(1, 2)
# 有返回值
print(func2())
