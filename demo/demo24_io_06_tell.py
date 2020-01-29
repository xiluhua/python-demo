'''
@author: xilh
@since: 20200128
'''
from demo.tools.tool import pline, Encoding

# 在文件末尾添加
with open(file="D:\\tmp\\test1.txt", mode="w", encoding=Encoding.GBK) as file:
    file.write("今天")
    print(file.tell())
    file.write("明天")
    print(file.tell())
    
with open(file="D:\\tmp\\test1.txt", mode="r") as file:
    # 读取所有内容
    content = file.read()
print("content:")
print(content) 
pline()

with open(file="D:\\tmp\\test.txt", mode="r") as file:
    # 读取所有内容
    content = file.read(1)
    print("content:", content)
    print(file.tell())
    # 从头开始读
    file.seek(0)
    print(file.tell())
    


