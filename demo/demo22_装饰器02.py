'''
多个装饰器: 先装饰下面的, 再装饰上面的
@author: xilh
@since: 20200127
'''
def make_bold(fn):
    print("1...")
    def inner():
        tmp = '<b>'+fn()+'</b>'
        print("2...", tmp)
        return tmp
    return inner

def make_italic(fn):
    def inner():
        tmp = '<i>'+fn()+'</b>'
        print("3...", tmp)
        return tmp
    return inner

def my_func1():
    return 'hello1'

@make_italic
@make_bold
def my_func2():
    return 'hello2'

@make_italic
@make_bold
def my_func3():
    return 'hello3'

print(my_func2())