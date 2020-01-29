'''
文件读取后自动关闭, 使用: with open() as
@author: xilh
@since: 20200128
'''
# 读取文件, 获取文件流对象
from demo.tools.tool import pline

with open(file="D:\\tmp\\test.txt", mode="r") as file:
    content = ''
    print("file.closed:", file.closed)
    # 读取所有内容
    while True:
        line = file.readline()
        if line == '':
            break
        content = content + line
print("content:")
print(content) 
print("file.closed:", file.closed)
pline()

with open(file="D:\\tmp\\test.txt", mode="r") as file:
    content = ''
    # 读取所有内容
    line = file.readlines()
    for i in line:
        content = content + i
print("content:")
print(content) 
pline()

with open(file="D:\\tmp\\test.jpg", mode="rb") as file:
    # 读取所有内容
    content = file.read()
print("content:")
print(content) 


