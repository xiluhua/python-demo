'''
装饰器
    - 在不修改源代码的情况下, 增加一些功能, 比如权限的验证 & 日志等等
@author: xilh
@since: 20200127
'''
def login(func):
    print("1...")
    def inner():
        print("2...")
        func()
    return inner

def add():
    print("add ...")
def delete():
    print("delete ...")
def update():
    print("update ...")
@login    
def select():
    print("select ...")

# 闭包实现
# ret = login(select, "admin", "123")
# ret()

# 装饰器实现
select()
# 无装饰器
update()